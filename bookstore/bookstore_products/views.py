from django.shortcuts import render
from django.views.generic import ListView
from .models import product
# Create your views here.


class productsList(ListView):
    template_name = './products_list.html'
    paginate_by = 1

    def get_queryset(self):
        return product.objects.get_active_products()


def productDetails(request):
    return render(request, './product_details.html',{})