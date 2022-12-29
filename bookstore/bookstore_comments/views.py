from django.shortcuts import render

from bookstore_products.models import Book

from .forms import CommentForm
from .models import Comments

# Create your views here.


def add_comment(request, *args, **kwargs):
  commentForm = CommentForm(request.POST or None)
  book_id = kwargs['bookId']
  book = Book.objects.get_by_id(book_id)
  if commentForm.is_valid():
    comment = commentForm.cleaned_data.get('comment')

    Comments.objects.create(
      user=request.user,
      book=book,
      comment=comment
    )
  context = {
    'comment':commentForm,
  }
  return render(request, '../bookstore_products/book_details.html', context)
