from django.contrib import admin
from .models import bookCategory
# Register your models here.

class bookCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__']

    class Meta:
        model = bookCategory

admin.site.register(bookCategory, bookCategoryAdmin)