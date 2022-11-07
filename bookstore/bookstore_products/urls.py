from django.urls import path
from .views import productsList,productDetails

urlpatterns = [
    path('books',productsList.as_view()),
    path('book-details',productDetails),
]