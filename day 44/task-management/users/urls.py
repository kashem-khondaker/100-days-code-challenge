from django.urls import path
from users.views import Sign_Up
urlpatterns = [
    path('sign-up/' , Sign_Up , name="sign-up"),
]
