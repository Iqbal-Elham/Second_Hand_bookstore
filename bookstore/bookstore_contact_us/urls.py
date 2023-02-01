from django.urls import path
from .views import contact_us

urlpatterns = [
    path('contact-us',contact_us),
]