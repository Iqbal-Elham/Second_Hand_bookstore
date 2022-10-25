from django.urls import path
from .views import login, register


urlpatterns = [
    path('log',login,name='log'),
    path('register',register)
]