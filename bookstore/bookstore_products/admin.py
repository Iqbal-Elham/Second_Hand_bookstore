from django.contrib import admin
from .models import Book
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price','active']

    class Meta:
        model = Book


admin.site.register(Book, productAdmin)