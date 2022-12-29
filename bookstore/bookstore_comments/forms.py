from django import forms
from django.core import validators

class CommentForm(forms.Form):

    comment = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder':"Enter your comment",'class':'form-control', 'rows':1})
    )