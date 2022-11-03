from django.urls import path
from .views import productsList

urlpatterns = [
    path('products',productsList.as_view()),
]