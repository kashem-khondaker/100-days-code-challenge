from django.contrib import admin
from tasks.models import Task,taskDetails ,Project

# Register your models here.
# class TaskAdmin(admin.ModelAdmin):
#     list_display = ('title', 'status', 'get_priority')

#     def get_priority(self, obj):

#         return obj.details.priority if hasattr(obj, 'details') else "Not Set"

#     get_priority.short_description = "Priority"
# admin.site.register(Task, TaskAdmin)

admin.site.register(Task)
admin.site.register(taskDetails)
admin.site.register(Project)

