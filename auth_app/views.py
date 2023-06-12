from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth.models import User
from post.models import Posts


# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Username already taken")
            return redirect(reverse('auth:register'))

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)

        user.save()
        messages.success(request, "User Created successfully")
        return redirect(reverse('auth:login'))

    return render(request, "auth_app/register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid username")
            return redirect(reverse('auth:login'))

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "invalid password")
            return redirect(reverse('auth:login'))

        else:
            login(request, user)
            return redirect(reverse('post:posts'))

    return render(request, "auth_app/login.html")


def logout_user(request):
    logout(request)
    return redirect(reverse('auth:login'))


def profile(request):
    if request.user.is_authenticated:
        user_name = request.user.username
        user = User.objects.get(username=user_name)
        print(user.id)
        posts = Posts.objects.filter(user=user)

    return render(request, "auth_app/profile.html", {
        "user": user,
        "posts": posts,
    })
