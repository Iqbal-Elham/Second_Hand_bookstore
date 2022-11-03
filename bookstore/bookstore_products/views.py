from django.shortcuts import render
from django.views.generic import ListView
from .models import product
# Create your views here.


class productsList(ListView):
    template_name = './products_list.html'

    def get_queryset(self):
        return product.objects.get_active_products()