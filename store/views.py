from django import forms
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import SignUpForm
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ("You are logged in"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, please try again"))
            return redirect('login')
        
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You are now logged out"))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Log In User
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You Have Registered"))
            return redirect('home')
        else:
             messages.success(request, ("There was a problem registering"))
             return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})


    


