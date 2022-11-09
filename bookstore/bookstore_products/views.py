from django.shortcuts import render
from django.views.generic import ListView
from .models import book
from django.http import Http404
# Create your views here.


class bookList(ListView):
    template_name = './books_list.html'
    paginate_by = 6

    def get_queryset(self):
        return book.objects.get_active_products()


def bookDetails(request, *args, **kwargs):
    book_id = kwargs['bookId']

    books = book.objects.get_by_id(book_id)

    if books is not None and books.active:
        context = {
            'books': books
                }
        return render(request, './book_details.html',context)
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

    