from django.urls import path
from .views import login_page, register,login_wave


urlpatterns = [
    path('register',register),
    path('login',login_wave),
    # path('login',login_page),
]