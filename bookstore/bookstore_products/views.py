import itertools
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
        book_category = bookCategory.objects.filter(title__iexact=category_name).first()

        if book_category is None:
            raise Http404("Page not Found")

        return book.objects.get_by_category(category_name)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def bookDetails(request, *args, **kwargs):
    book_id = kwargs['bookId']

    books = book.objects.get_by_id(book_id)
    print(books)

    if books is None or not books.active:
        raise Http404

    related_books = book.objects.get_queryset().filter(category__book=books).distinct()
    print(related_books)
    grouped_related_books = my_grouper(4, related_books)
    grouped_related_books = list(grouped_related_books)
    print(grouped_related_books)
    context = {
        'books': books,
        'related_books': grouped_related_books,
    }
    return render(request, './book_details.html', context)


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
