from django import forms 
from django.contrib.auth.models import User

class dateInput(forms.DateInput):
    input_type = 'date'

class sellBookForm(forms.Form):

  book_name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-4", "placeholder":"Enter your Book Name"}),
        label="Book Name"
    )
  book_author = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-4", "placeholder":"Enter your Book Author"}),
        label="Book Author"
    )
  book_publisher = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-4", "placeholder":"Enter your Book Publisher"}),
        label="Book Publisher"
    )
  book_edition = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-4", "placeholder":"Enter your Book Edition"}),
        label="Book Edition"
    )
  book_language = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-4", "placeholder":"Enter language of your Book"}),
        label="Book language"
    )
  price = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-4", "placeholder":"Enter your Book Price"}),
        label="Book Price"
    )
  CHOICES =(
    (1, "Novel"),
    (2, "History"),
    (3, "Politics"),
    (4, "Psychology"),
    (5, "Philosophy"),
    (6, "Literature"),
    (7, "Medical"),
    (8, "Computer"),
    (9, "Economic"),
    (10, "Sport"),
    (11, "Management"),
    (12, "Engineering"),
    (13, "Social"),
    (14, "Law"),
    (15, "Languages"),
    (16, "other"),
)
  category = forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-select mb-4",}),
        choices=CHOICES, 
        label="Category"
    )
  date = forms.DateField(
        widget=dateInput,

    )
  description = forms.CharField(
    widget=forms.Textarea(attrs={'rows':"3",'class':'form-control mb-5', 'placeholder':'Tell us about your Experience for Studying'}),
    label = "description"
  )
  book_pic = forms.ImageField(
        widget=forms.FileInput(attrs={"class":"form-control mb-4","id":"file"})
    )
    

