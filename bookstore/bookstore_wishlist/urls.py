from django.urls import path
from .views import wish_list

urlpatterns = [
    path('wishlist', wish_list),
]