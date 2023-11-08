from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.utils.safestring import mark_safe

# Create your models here.




class CustomUser(AbstractUser):
    CHOICES_TYPE = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    phone_num = models.BigIntegerField(null = True, blank= True)
    user_type = models.CharField(max_length=15, choices = CHOICES_TYPE)
    profile = models.ImageField(upload_to = 'profile_pictures/', null = True, blank = True, default= None)

    objects = UserManager()

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width = "50", height = "50" />' % (self.profile))