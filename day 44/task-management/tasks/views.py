from django.shortcuts import render , redirect,get_object_or_404
from django.db.models import Q , Count , Max , Min , Avg
from django.contrib import messages
from django.http import HttpResponse
from datetime import date
from tasks.forms import TaskForm , TaskModelForm,TaskDetailsModelForm
from tasks.models import Employee , Task , taskDetails,Project

# Create your views here.

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

def user_dashboard(request):
    return render(request, "dashboard/user_dash_board.html")

def test(request):
    context = {
        "name": ["kashem" , "rakib" , "rashed"],
        "age":23
    }
    return render(request , 'test.html' , context)


def show_task(request):
    return ("this is show task")

def create_task(request):
    # employee = Employee.objects.all()
    task_form = TaskModelForm()
    task_detail_form = TaskDetailsModelForm()
    
    if request.method == "POST":
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailsModelForm(request.POST)
        print(task_form)
        print(task_detail_form)
        
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



def update_task(request, id):
    task = get_object_or_404(Task, id=id)

    task_details, created = taskDetails.objects.get_or_create(task=task)

    task_form = TaskModelForm(instance=task)
    task_detail_form = TaskDetailsModelForm(instance=task_details)

    if request.method == "POST":
        task_form = TaskModelForm(request.POST, instance=task)
        task_detail_form = TaskDetailsModelForm(request.POST, instance=task_details)

        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_details = task_detail_form.save(commit=False)
            task_details.task = task
            task_details.save()

            messages.success(request, "Task Updated Successfully")
            return redirect('update-task', id=id)

    context = {'task_form': task_form, "task_detail_form": task_detail_form}
    return render(request, "dashboard/task_form.html", context)

def delete_task(request,id):
    if request.method=='POST':
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, "Task Deleted Successfully")
        return redirect('manager-dashboard')
    else:
        messages.error(request,'Something went Wrong')
        return redirect('manager-dashboard')

def view_task(request):
    # tasks = Task.objects.all()

    # filter data by status are Pending
    # tasks = Task.objects.filter(status = "PENDING")

    # filter data by date 
    # tasks = Task.objects.filter(due_date = date.today())

    # filter data by priority is not low 
    # tasks = taskDetails.objects.exclude(priority = 'Low')
    # tasks = Task.objects.filter(due_date__lte="2025-01-09")

    # employee = Employee.objects.get(id=47)
    # tasks = Task.objects.filter(employee = employee)

    # project = Project.objects.get(id=2)
    # employees = Employee.objects.filter(task__project=project).distinct()
    # today = date.today()
    # tasks = Task.objects.filter(due_date=today)
    # tasks = Task.objects.filter(taskDetails__priority__in=['Low', 'Medium'])
    # tasks = Task.objects.exclude(taskdetails__priority = 'low')
    employee = Employee.objects.get(id=1)
    tasks = Task.objects.filter(employee=employee , is_completed=True)
    return render(request , 'view_task.html' , {'tasks':tasks })
    # return render(request, "view_task.html" , {'employees': employees})
    # pass

def view_employee_tasks(request,employee_id ):
    employee = Employee.objects.get(id =employee_id)
    employee_tasks = Task.objects.filter(employee=employee)
    return render(request, "view_task.html" , {"tasks": employee_tasks , "employee":employee})