from django.contrib import admin

from bookstore_wishlist.models import Wish, wishDetail

# Register your models here.


admin.site.register(Wish)
admin.site.register(wishDetail)
