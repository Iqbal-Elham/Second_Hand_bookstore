import itertools
from django.shortcuts import render
from django.views.generic import ListView

from bookstore_category.models import bookCategory
from bookstore_wishlist.forms import userWishlistForm
from .models import Book
from .forms import sellBookForm
from django.http import Http404
# Create your views here.


class bookList(ListView):
    template_name = './books_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Book.objects.get_active_products()


class books_by_category(ListView):
    template_name = './books_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['category_title']
        book_category = bookCategory.objects.filter(title__iexact=category_name).first()

        if book_category is None:
            raise Http404("Page not Found")

        return Book.objects.get_by_category(category_name)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def bookDetails(request, *args, **kwargs):

    book_id = kwargs['bookId']
    new_wish_form = userWishlistForm(request.POST or None, initial={'book_id': book_id})

    books = Book.objects.get_by_id(book_id)

    if books is None or not books.active:
        raise Http404

    books.visit_count += 1
    books.save()

    related_books = Book.objects.get_queryset().filter(category__book=books).distinct()
    grouped_related_books = my_grouper(4, related_books)
    grouped_related_books = list(grouped_related_books)
    context = {
        'books': books,
        'related_books': grouped_related_books,
        'wish_form' :new_wish_form,
    }
    return render(request, './book_details.html', context)


class searchBookView(ListView):

    template_name = './books_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q')
        if query is None:
            return Book.objects.get_active_products()

        return Book.objects.search(query)


def category_partial(request):
    categories = bookCategory.objects.all()
    context = {
        'categories': categories,
    }

    return render(request, './category_partial.html', context)

def sellBook(request):
    sellForm = sellBookForm(request.POST or None, request.FILES or None)
    if sellForm.is_valid():
        bookName = sellForm.cleaned_data.get('book_name')
        book_author = sellForm.cleaned_data.get('book_author')
        book_publisher = sellForm.cleaned_data.get('book_publisher')
        book_edition = sellForm.cleaned_data.get('book_edition')
        book_language = sellForm.cleaned_data.get('book_language')
        price = sellForm.cleaned_data.get('price')
        category = sellForm.cleaned_data.get('category')
        date = sellForm.cleaned_data.get('date')
        book_pic = sellForm.cleaned_data.get('book_pic')
        description = sellForm.cleaned_data.get('description')
        instance = Book.objects.create(
            title=bookName,
            Author=book_author,
            publisher=book_publisher,
            edition=book_edition,
            price=price,
            language=book_language,
            Date=date,
            description=description,
            image=book_pic,
        )

        instance.category.add(category)
        sellForm = sellBookForm()

    context = {
        'sellForm': sellForm
    }
    return render(request, 'sell_book.html', context)