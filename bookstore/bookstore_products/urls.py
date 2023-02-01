from django.urls import path
from .views import bookList,bookDetails, searchBookView, books_by_category, category_partial, sellBook

urlpatterns = [
    path('books',bookList.as_view()),
    path('books/<category_title>/',books_by_category.as_view()),
    path('books/<bookId>/<name>',bookDetails),
    path('books/search', searchBookView.as_view()),
    path('category_partial', category_partial, name="category_partial"),
    path('sell-book', sellBook),
]