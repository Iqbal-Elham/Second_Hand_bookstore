from django.shortcuts import render

# Create your views here.

def login(request):
    context = {}
    return render(request, 'account/login.html',context)

def register(request):
    context = {}
    return render(request, 'account/register.html',context)

