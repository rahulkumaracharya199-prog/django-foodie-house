from django.shortcuts import render, redirect
from foodie.models import Category, Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm as LoginForm
from django.contrib.auth import login, logout, authenticate


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        newUser = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )
        newUser.save()
        return redirect ("login")
    return render(request, "registration/signup.html")

def loginView(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("homepage")
    else:
        form = LoginForm()
        
    return render(request, "registration/login.html", {"form":form})


def logoutView(request):
    logout(request)
    return redirect("homepage")

