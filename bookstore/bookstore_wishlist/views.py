from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Wish, wishDetail
from bookstore_products.models import Book
from bookstore_wishlist.forms import userWishlistForm

@login_required(login_url='/login')
def add_user_wish(request):
    new_wish_form = userWishlistForm(request.POST or None)

    if new_wish_form.is_valid():
        
        wish = Wish.objects.filter(owner_id=request.user.id).first()
        if wish is None:
            wish = Wish.objects.create(owner_id=request.user.id)
        
        book_id = new_wish_form.cleaned_data.get('book_id')
        bookk = Book.objects.get_by_id(book_id=book_id)
        # search = Wish.objects.filter(owner_id=request.user, )
        wish.wishdetail_set.create(wishBook_id = bookk.id,price=bookk.price)
        return redirect(f'/books/{bookk.id}/{bookk.title.replace(" ", "-")}')

    return redirect('/books')

@login_required(login_url='/login')
def wish_list(request, *args, **kwargs):
    context = {
        'wish' : None,
        'details' : None,
    }
    open_wish = Wish.objects.filter(owner_id=request.user.id).first()
    if open_wish is not None :
        context['wish'] = open_wish
        context['details'] = open_wish.wishdetail_set.all()
    print(len(context['details']))
    return render(request, 'wish_list.html', context)



@login_required(login_url='/login')
def remove_wish_item(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        wish_detail = wishDetail.objects.get_queryset().get(id=detail_id, wish__owner_id=request.user.id)
        if wish_detail is not None:
            wish_detail.delete()
    return redirect('/wishlist')