from django.urls import path
from .views import bookList,bookDetails, searchBookView

urlpatterns = [
    path('books',bookList.as_view()),
    path('books/<bookId>/<name>',bookDetails),
    path('books/search', searchBookView.as_view()),
]