from django.shortcuts import render , redirect
from django.db.models import Q , Count , Max , Min , Avg
from django.contrib import messages
from django.http import HttpResponse
from datetime import date
from tasks.forms import TaskForm , TaskModelForm,TaskDetailsModelForm
from tasks.models import  Task , taskDetails,Project
from django.contrib.auth.decorators import login_required , user_passes_test , permission_required
from users.views import is_admin
from django.views import View
# Create your views here.


def is_manager(user):
    return user.groups.filter(name="Manager").exists()


def is_employee(user):
    return user.groups.filter(name="Employee").exists()

def is_admin(user):
    return user.groups.filter(name="Admin").exists()

def is_manager_or_admin(user):
    return is_admin(user) or is_manager(user)



# @login_required
@user_passes_test(is_manager_or_admin , login_url='no_permission')
def manager_dashboard(request):
    
    base_query = Task.objects.select_related('details').prefetch_related('employee')

    type = request.GET.get('type','all')

    if type =="completed":
        # tasks = Task.objects.select_related('details').prefetch_related('employee').filter(status = "COMPLETED")
        tasks = base_query.filter(status = "COMPLETED")
    elif type=="in_progress":
        tasks = base_query.filter(status= "IN_PROGRESS")
    elif type=="pending":
        tasks = base_query.filter(status = "PENDING")
    elif type =="all":
        tasks = base_query.all()
    
    counts = Task.objects.aggregate(
        total=Count('id'),
        pending=Count('id', filter=Q(status='PENDING')),
        in_progress=Count('id', filter=Q(status='IN_PROGRESS')),
        completed=Count('id', filter=Q(status='COMPLETED')),
    )
    context = {
        "tasks":tasks,
        "counts":counts
    }
    return render(request , "dashboard/manager-dashboard.html" , context)


@user_passes_test(is_employee)
def Employee_dashboard(request):
    return render(request, "dashboard/user_dash_board.html")

def test(request):
    context = {
        "name": ["kashem" , "rakib" , "rashed"],
        "age":23
    }
    return render(request , 'test.html' , context)


# def show_task(request):
#     return ("this is show task")


@login_required
@permission_required("tasks.add_task", login_url='no-permission')
def create_task(request):
    # employee = Employee.objects.all()
    task_form = TaskModelForm()
    task_detail_form = TaskDetailsModelForm()
    
    if request.method == "POST":
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailsModelForm(request.POST, request.FILES)
        # print(task_form)
        # print(task_detail_form)
        
        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            print("1")
            task_detail.save()
            print('2')

            messages.success(request,"Task Create Successfully")
            return redirect('create-task')
    
    context = {'task_form':task_form , "task_detail_form":task_detail_form}
    return render(request , "dashboard/task_form.html" , context)

class CreateTask(View):

    template_name = 'task_form.html'

    def get(self , request , *args , **kwargs):
        task_form = TaskModelForm()
        task_detail_form = TaskDetailsModelForm()

        context = {'task_form':task_form , "task_detail_form":task_detail_form}
        return render(request , "dashboard/task_form.html" , context)
    

    def post(self , request , *args , **kwargs):
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailsModelForm(request.POST, request.FILES)

        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request,"Task Create Successfully")
            return redirect('create-task')





@login_required
@permission_required("tasks.change_task", login_url='no-permission')
def update_task(request , id):
    
    task = Task.objects.get(id=id)
    task_form = TaskModelForm(instance = task)
    task_detail_form = TaskDetailsModelForm(instance=task.details)
    
    if request.method == "POST":
        task_form = TaskModelForm(request.POST , instance=task)
        task_detail_form = TaskDetailsModelForm(request.POST,instance=task.details)
        
        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request,"Task Update Successfully")
            return redirect('update-task',id=id)

    context = {'task_form':task_form , "task_detail_form":task_detail_form}
    return render(request , "dashboard/task_form.html" , context)

def task_details(request , task_id):
    task = Task.objects.get(id = task_id)
    return render(request , 'task_details.html' , {'task':task})

@login_required
@permission_required("tasks.delete_task", login_url='no-permission')
def delete_task(request,id):
    if request.method=='POST':
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, "Task Deleted Successfully")
        return redirect('manager-dashboard')
    else:
        messages.error(request,'Something went Wrong')
        return redirect('manager-dashboard')
    
@login_required
def dashboard(request):
    if is_manager(request.user):
        return redirect('manager-dashboard')
    elif is_employee(request.user):
        return redirect('user_dashboard')
    elif is_admin(request.user):
        return redirect('Admin_dashboard')
    
    return redirect('no_permission')



@login_required
@permission_required("tasks.view_task", login_url='no-permission')
def view_task(request):

    employee = Employee.objects.get(id=1)
    tasks = Task.objects.filter(employee=employee , is_completed=True)
    return render(request , 'view_task.html' , {'tasks':tasks })



@login_required
@permission_required("tasks.view_task" , login_url='no_permission')
def view_employee_tasks(request,employee_id ):
    employee = Employee.objects.get(id =employee_id)
    employee_tasks = Task.objects.filter(employee=employee)
    return render(request, "view_task.html" , {"tasks": employee_tasks , "employee":employee})
