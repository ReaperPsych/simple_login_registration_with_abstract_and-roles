from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def home_view(request, ):
    if request.user.is_authenticated:
        first_name = request.user.first_name
    else:
        first_name = ''


    return render (request, 'home.html', {'first_name': first_name})

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        phone_number = request.POST['phone_number']
        user_type = request.POST['user_role']

        if password != confirm_password:
            messages.error(request, "Password and Confirm Password didn't match")
            return redirect('signup')

        myuser = CustomUser.objects.create_user(username=username, email=email, password=password)

        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.phone_number = phone_number
        myuser.user_type = user_type
        myuser.save()

        messages.success(request, 'Your account has been created successfully')
        
        return redirect('login')
    
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/')
        
        else:
            messages.error(request, 'Invalid Credentials, Please try again')
            return redirect('login')

        
        
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')