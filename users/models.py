from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.

class CustomUser(AbstractUser):
    CHOICES_TYPE = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    phone_num = models.BigIntegerField(null = True, blank= True)
    user_type = models.CharField(max_length=15, choices = CHOICES_TYPE)

    objects = UserManager()