from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from .forms import login_form

# Create your views here.

def login_page(request):
    form = login_form(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get("user_name")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
    context = {
        "loginForm" : form 
    }
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, 'account/login.html',context)

def register(request):
    context = {}
    return render(request, 'account/register.html',context)

