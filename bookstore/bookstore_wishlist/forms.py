from django import forms




class userWishlistForm(forms.Form):

  book_id = forms.IntegerField(
    widget=forms.HiddenInput()
  )