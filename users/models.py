from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from PIL import Image

# Create your models here.




class CustomUser(AbstractUser):
    CHOICES_TYPE = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    phone_num = models.BigIntegerField(null = True, blank= True)
    user_type = models.CharField(max_length=15, choices = CHOICES_TYPE)
    profile = models.FileField(upload_to = 'profile_pictures/', null = True, blank = True, default= None)

    objects = UserManager()