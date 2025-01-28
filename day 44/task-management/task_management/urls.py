from django.contrib import admin
from debug_toolbar.toolbar import debug_toolbar_urls
from django.urls import path ,include
from tasks.views import manager_dashboard


urlpatterns = [
    path('my-admin/' , admin.site.urls),
    path('tasks/' , include("tasks.urls"))
]+ debug_toolbar_urls()
