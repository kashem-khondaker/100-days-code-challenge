from django.contrib import admin
from django.urls import path
from tasks.views import manager_dashboard , user_dashboard ,test , create_task ,view_task ,view_employee_tasks,update_task,delete_task


urlpatterns = [
    # path('admin/' , admin.site.urls),
    path('manager_dashboard/',manager_dashboard , name="manager-dashboard"),
    path('user-dashboard/' ,user_dashboard),
    path('test/' , test),
    path('task-html/' , create_task , name='create-task'),
    path('update-task/<int:id>/' , update_task , name='update-task'),
    path('delete-task/<int:id>/' , delete_task , name='delete-task'),
    path('view_task/',view_task),
    path('employee/<int:employee_id>/' , view_employee_tasks ,name = "view_employee_task")
]
