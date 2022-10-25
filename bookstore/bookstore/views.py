import code
from django.shortcuts import render

# footer back code
def footer(request):
    context = {}
    return render(request,'shared/footer.html',context)

def home_page(request):

    return render(request, './index.html', {})