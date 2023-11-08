from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None ,{'fields':('username', 'email', 'password')}),
        ('Personal Information', {'fields':('first_name', 'last_name', 'phone_num', 'profile')}),
        ('User Type', {'fields':('user_type',)}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'user_type', 'profile', 'image_tag']


