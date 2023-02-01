from django import forms
from django.core import validators

class contactUs_form(forms.Form):

    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':"Enter your Fullname",'class':'form-control'}),
        validators=[validators.MaxLengthValidator(150,'Max length of character is 150')]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':"Enter your Email",'class':'form-control mb-2'}),
        validators=[validators.MaxLengthValidator(150,'Max length of character is 150')]
    )
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':"Enter the Subject",'class':'form-control'}),
        validators=[validators.MaxLengthValidator(100,'Max length of character is 100')]
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':"Enter your message",'class':'form-control', 'rows':6})
    )