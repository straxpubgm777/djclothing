from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from users.models import *


def login(request):
    email = None
    password = None
    error_message = None

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('app:home_page_url')
        else:
            error_message = "Email or password is wrong"

    return render(request, 'login.html', {"error_message": error_message})


def signout(request):
    logout(request)
    return redirect('app:home_page_url')