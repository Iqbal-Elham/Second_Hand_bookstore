from django.contrib import admin
from .models import contactUs
# Register your models here.



class contactAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'full_name', 'is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    search_fields = ['subject', 'message']

admin.site.register(contactUs, contactAdmin)