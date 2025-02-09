from django.contrib import admin
from tasks.models import Task,taskDetails , Employee,Project

# Register your models here.
admin.site.register(Task)
admin.site.register(taskDetails)
admin.site.register(Employee)
admin.site.register(Project)

