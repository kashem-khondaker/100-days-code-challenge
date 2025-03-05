from django.contrib import admin
from django.urls import path
from tasks.views import manager_dashboard , Employee_dashboard ,test , create_task ,view_task ,view_employee_tasks,update_task,delete_task,task_details,dashboard ,CreateTask , ViewProject,TaskDetail,UpdateTask , ManagerDashboardView


urlpatterns = [
    path('manager_dashboard/',ManagerDashboardView.as_view() , name="manager-dashboard"),
    path('user-dashboard/' ,Employee_dashboard , name='user_dashboard'),
    path('test/' , test),
    path('create/' , CreateTask.as_view() , name='create-task'),
    path('update-task/<int:id>/' , UpdateTask.as_view() , name='update-task'),
    path('delete-task/<int:id>/' , delete_task , name='delete-task'),
    path('view_task/',view_task , name="view_task"),
    path('view-projects/' , ViewProject.as_view() , name="view_project"),
    path('employee/<int:employee_id>/' , view_employee_tasks ,name = "view_employee_task"),
    path('task_details/<int:task_id>' , TaskDetail.as_view() , name="task_details"),
    path('dashboard/' , dashboard , name='dashboard'),
    # path('admin/' , admin.site.urls),
    # path('manager_dashboard/',manager_dashboard.as_view() , name="manager-dashboard"),
    # path('create/' , create_task , name='create-task'),
    # path('update-task/<int:id>/' , update_task , name='update-task'),
    # path('task_details/<int:task_id>' , task_details , name="task_details"),
]
