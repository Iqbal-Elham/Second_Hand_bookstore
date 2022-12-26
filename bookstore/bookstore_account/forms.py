from django import forms 
from django.contrib.auth.models import User


class login_form(forms.Form):

    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"box","placeholder":"Enter your username"}),
        label="Username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"box","placeholder":"Enter your password"}),
        label="Password"
    )

class dateInput(forms.DateInput):
    input_type = 'date'

class register_form(forms.Form):

    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your username"}),
        
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter your email"}),
        
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter your password"}),
        
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter your password again"}),
        
    )

    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_is_exist = User.objects.filter(email=email).exists()
        if email_is_exist:
            raise forms.ValidationError("Email is exist")
        return email

    def clean_user_name(self):
        username = self.cleaned_data.get("user_name")
        username_is_exist = User.objects.filter(username=username).exists()
        if username_is_exist:
            raise forms.ValidationError("Username is exist")
        return username
    
    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")

        if password != re_password:
            raise forms.ValidationError("Passwords does not match")
        
        return password

class editRegisterForm(forms.Form):
    
    profile_pic = forms.ImageField(
        widget=forms.FileInput(attrs={"id":"file"})
    )
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your username"}),
        
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter your email"}),
        
    )
    date_of_birth = forms.DateField(
        widget=dateInput,

    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your city"}),

    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your address"}),
    
    )
    CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=CHOICES, 
        
    )
    phone_num = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your phone number"}),
    
    )
    whatsapp_num = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your whatsapp number"}),
    
    )