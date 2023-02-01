import code
import itertools
from django.shortcuts import render

from bookstore_products.models import Book

# footer back code
def footer(request):
    context = {}
    return render(request,'shared/footer.html',context)

def grouper(n, iterable):
    args = [iter(iterable)]
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

def home_page(request):
    most_visit_books = Book.objects.order_by('-visit_count').all()[:10]
    latest_books = Book.objects.order_by('-id').all()[:5]
    latest_books2 = Book.objects.order_by('-id').all()[5:10]
    grouped_visited_books = grouper(10, most_visit_books)
    grouped_visited_books = list(grouped_visited_books)
    grouped_latest_books = grouper(5, latest_books)
    grouped_latest_books = list(grouped_latest_books)

    grouped_latest_books2 = grouper(5, latest_books2)
    grouped_latest_books2 = list(grouped_latest_books2)
    context = {
        'most_visited' : grouped_visited_books,
        'latest_books' : grouped_latest_books,
        'latest_books2' : grouped_latest_books2,
    }
    return render(request, './index.html', context)