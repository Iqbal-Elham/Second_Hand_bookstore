from django.urls import path
from .views import log_out, login_page, register,login_wave


urlpatterns = [
    path('register',register),
    path('login',login_wave),
    path('logout',log_out),
]