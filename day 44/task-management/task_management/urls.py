from django.contrib import admin
from debug_toolbar.toolbar import debug_toolbar_urls
from django.urls import path ,include
from tasks.views import manager_dashboard
from core.views import home


urlpatterns = [
    path('my-admin/' , admin.site.urls),
    path('' , home , name="home"),
    path('tasks/' , include("tasks.urls")),
    path('users/',include("users.urls"))
]+ debug_toolbar_urls()
