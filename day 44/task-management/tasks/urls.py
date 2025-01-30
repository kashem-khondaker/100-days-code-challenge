from django.contrib import admin
from django.urls import path
from tasks.views import manager_dashboard , user_dashboard ,test , create_task ,view_task ,view_employee_tasks


urlpatterns = [
    path('admin/' , admin.site.urls),
    path('manager_dashboard/',manager_dashboard),
    path('user-dashboard/' ,user_dashboard),
    path('test/' , test),
    path('task-html/' , create_task),
    path('view_task/',view_task),
    path('employee/<int:employee_id>/' , view_employee_tasks ,name = "view_employee_task")
]
