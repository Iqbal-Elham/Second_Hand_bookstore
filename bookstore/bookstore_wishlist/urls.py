from django.urls import path
from .views import add_user_wish, remove_wish_item, wish_list

urlpatterns = [
    path('wishlist', wish_list),
    path('user-wishlist', add_user_wish),
    path('remove-wishlist-item/<detail_id>', remove_wish_item), 
]