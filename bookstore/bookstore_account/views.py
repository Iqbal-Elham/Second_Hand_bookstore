from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.models import User
from .forms import login_form, register_form

# Create your views here.

def login_page(request):
    form = login_form(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get("user_name")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
        else:
            form.add_error("user_name", "Username not Found")
    context = {
        "loginForm" : form 
    }
    if request.user.is_authenticated:
        return redirect("/")
        
    return render(request, 'account/login.html',context)

def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    registerForm = register_form(request.POST or None)
    
    if registerForm.is_valid():
        username = registerForm.cleaned_data.get("user_name")
        email = registerForm.cleaned_data.get("email")
        password = registerForm.cleaned_data.get("password")
        city = registerForm.cleaned_data.get("city")
        address = registerForm.cleaned_data.get("address")
        phone_num = registerForm.cleaned_data.get("phone_num")
        whatsapp_num = registerForm.cleaned_data.get("whtatsapp_num")
        User.objects.create_user(username=username,email=email,password=password)
        return redirect("/")
    context = {
        'registerForm' : registerForm,
    }
    return render(request, 'account/register.html',context)



def login_wave(request):
    form = login_form(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get("user_name")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
        else:
            form.add_error("user_name", "Username not Found")
    context = {
        "loginForm" : form 
    }
    if request.user.is_authenticated:
        return redirect("/")
        
    return render(request, 'account/login_wave.html',context)