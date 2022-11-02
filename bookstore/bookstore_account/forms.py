from django import forms 


class login_form(forms.Form):

    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"box","placeholder":"Enter your username"}),
        label="Username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"box","placeholder":"Enter your password"}),
        label="Password"
    )

class register_form(forms.Form):

    user_name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"box","placeholder":"Enter your username"}),
        label="Username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class":"box","placeholder":"Enter your password"}),
        label="Password"
    )