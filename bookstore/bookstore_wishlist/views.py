from django.shortcuts import render

# Create your views here.

def wish_list(request):
    
    return render(request, 'wish_list.html', {})
