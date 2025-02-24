from django.contrib import admin
from debug_toolbar.toolbar import debug_toolbar_urls
from django.urls import path ,include
from tasks.views import manager_dashboard
from core.views import home , no_permission
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('my-admin/' , admin.site.urls),
    path('' , home , name="home"),
    path('tasks/' , include("tasks.urls")),
    path('users/',include("users.urls")),
    path('no-permission/' , no_permission , name="no_permission"),
]+ debug_toolbar_urls()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
