from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm , TaskModelForm
from tasks.models import Employee , Task 

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

            ''' this is form '''
            # data = form.cleaned_data
            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # employee = data.get('employee')
            # # print(data)

            # task = Task.objects.create(
            #     title = title,
            #     description = description,
            #     due_date = due_date,
            # )
            
            # # assign employee 
            # for emp_id in employee:
            #     get_emp = Employee.objects.get(id = emp_id)
            #     task.employee.add(get_emp)
            # return HttpResponse("Task added successfully!")
    
    context = {'form':form}
    return render(request , "dashboard/task_form.html" , context)