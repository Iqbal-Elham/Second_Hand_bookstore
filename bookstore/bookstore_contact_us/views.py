from django.shortcuts import render
from .forms import contactUs_form
from .models import contactUs

# Create your views here.


def contact_us(request):
    contactForm = contactUs_form(request.POST or None)

    if contactForm.is_valid():
        full_name = contactForm.cleaned_data.get('full_name')
        email = contactForm.cleaned_data.get('email')
        subject = contactForm.cleaned_data.get('subject')
        message = contactForm.cleaned_data.get('message')
        contactUs.objects.create(full_name=full_name, email=email,subject=subject,message=message,is_read=False)
        contactForm = contactUs_form()
    
    context = {
        'contactForm' : contactForm
    }
    return render(request, 'contact-us.html', context)