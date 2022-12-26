from django.urls import path
from .views import log_out, login_page, register,login_wave, user_account


urlpatterns = [
    path('register',register),
    path('login',login_wave),
    path('logout',log_out),
    path('user',user_account),
]