from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm , TaskModelForm
from tasks.models import Employee , Task , taskDetails
from datetime import date

# Create your views here.

def manager_dashboard(request):
    return render(request , "dashboard/manager-dashboard.html")

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
    form = TaskModelForm()
    
    if request.method == "POST":
        form = TaskModelForm(request.POST )
        if form.is_valid():
            form.save()
            return render(request , 'dashboard/task_form.html' , {"form": form , "message": "task added successfully!"} )

    
    context = {'form':form}
    return render(request , "dashboard/task_form.html" , context)

def view_task(request):
    # tasks = Task.objects.all()

    # filter data by status are Pending
    # tasks = Task.objects.filter(status = "PENDING")

    # filter data by date 
    # tasks = Task.objects.filter(due_date = date.today())

    # filter data by priority is not low 
    # tasks = taskDetails.objects.exclude(priority = 'Low')
    # tasks = Task.objects.filter(due_date__lte="2025-01-09")
    # return render(request , 'view_task.html' , {'tasks':tasks })
    pass

def view_employee_tasks(request,employee_id ):
    employee = Employee.objects.get(id =employee_id)
    employee_tasks = Task.objects.filter(employee=employee)
    return render(request, "view_task.html" , {"tasks": employee_tasks , "employee":employee})