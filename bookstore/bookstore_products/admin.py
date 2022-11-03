from django.contrib import admin
from .models import product
# Register your models here.

class productAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price','active']

    class Meta:
        model = product


admin.site.register(product, productAdmin)