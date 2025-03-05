from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_image' , blank=True , default='profile_images/default_img.jpg')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
