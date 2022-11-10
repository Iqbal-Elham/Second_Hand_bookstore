from django.shortcuts import render
from django.views.generic import ListView

from bookstore_category.models import bookCategory
from .models import book
from django.http import Http404
# Create your views here.


class bookList(ListView):
    template_name = './books_list.html'
    paginate_by = 6

    def get_queryset(self):
        return book.objects.get_active_products()


class books_by_category(ListView):
    template_name = './books_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['category_title']
        book_category = bookCategory.objects.filter(title__iexact = category_name).first()

        if book_category is None:
            raise Http404("Page not Found")

        return book.objects.get_by_category(category_name)


def bookDetails(request, *args, **kwargs):
    book_id = kwargs['bookId']

    books = book.objects.get_by_id(book_id)

    if books is not None and books.active:
        context = {
            'books': books
        }
        return render(request, './book_details.html', context)
    raise Http404


class searchBookView(ListView):

    template_name = './books_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is None:
            return book.objects.get_active_products()

        return book.objects.search(query)


def category_partial(request):
    categories = bookCategory.objects.all()
    context = {
        'categories': categories,
    }

    return render(request, './category_partial.html', context)