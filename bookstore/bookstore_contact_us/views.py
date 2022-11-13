from django.shortcuts import render

# Create your views here.


def contact_us(request):
    
    context = {

    }
    return render(request, 'contact-us.html',context)