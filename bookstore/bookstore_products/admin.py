from django.contrib import admin
from .models import book
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price','active']

    class Meta:
        model = book


admin.site.register(book, productAdmin)