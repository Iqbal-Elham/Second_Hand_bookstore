from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.models import User
from .forms import editRegisterForm, login_form, register_form

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
        User.objects.create_user(username=username, email=email, password=password)
        return redirect("/login")
    context = {
        'registerForm' : registerForm,
    }
    return render(request, 'account/register_wave.html',context)



def login_wave(request):
    registerForm = register_form(request.POST or None)
    if registerForm.is_valid():
        username = registerForm.cleaned_data.get("user_name")
        email = registerForm.cleaned_data.get("email")
        password = registerForm.cleaned_data.get("password")
        User.objects.create_user(username=username, email=email, password=password)
        return redirect("/login")
    
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
        "loginForm" : form,
        'registerForm' : registerForm,
    }
    if request.user.is_authenticated:
        return redirect("/")
        
    return render(request, 'account/login_wave.html',context)


def log_out(request):
    logout(request)
    return redirect("/")


def user_account(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    editForm = editRegisterForm(request.POST or None, request.FILES or None, 
    initial={
        'user_name':user.username, 
        'email':user.email,
        'profile_pic':user.user_profile.profile_pic,
        'date_of_birth':user.user_profile.date_of_birth,
        'city':user.user_profile.city,
        'address':user.user_profile.address,
        'gender':user.user_profile.gender,
        'phone_num':user.user_profile.phone_num,
        'whatsapp_num':user.user_profile.whatsapp_num,
        })
    if editForm.is_valid():
        profile_pic = editForm.cleaned_data.get('profile_pic')
        user_name = editForm.cleaned_data.get('user_name')
        email = editForm.cleaned_data.get('email')
        date_of_birth = editForm.cleaned_data.get('date_of_birth')
        city = editForm.cleaned_data.get('city')
        address = editForm.cleaned_data.get('address')
        gender = editForm.cleaned_data.get('gender')
        phone_num = editForm.cleaned_data.get('phone_num')
        whatsapp_num = editForm.cleaned_data.get('whatsapp_num')
        user.username = user_name
        user.email = email
        user.user_profile.date_of_birth = date_of_birth
        user.user_profile.city = city
        user.user_profile.address = address
        user.user_profile.gender = gender
        user.user_profile.phone_num = phone_num
        user.user_profile.whatsapp_num = whatsapp_num
        user.user_profile.profile_pic = profile_pic
        user.save()
        user.user_profile.save()
        

    context = {
            'editForm' : editForm,
            'profile_pic' :user,
        }

    return render(request, './user_account.html', context)