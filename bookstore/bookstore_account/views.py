from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from bookstore_products.forms import sellBookForm
from bookstore_products.models import Book
from django.contrib import messages
from .models import user_profile
from .forms import editRegisterForm, login_form, register_form, MyPasswordChangeForm


# Create your views here.


def register(request):
    registerForm = register_form(request.POST or None)
    if registerForm.is_valid():
        username = registerForm.cleaned_data.get("user_name")
        email = registerForm.cleaned_data.get("email")
        password = registerForm.cleaned_data.get("password")
        instanceUser = User.objects.create_user(username=username, email=email, password=password)
        user_profile.objects.create(user=instanceUser)
        return redirect("/login")
    context = {
        'registerForm' : registerForm,
    }
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, 'account/register_wave.html',context)



def login_wave(request):
    form = login_form(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("user_name")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
        else:
            form.add_error("password", "Password does not match")
    context = {
        "loginForm" : form,
    }
    if request.user.is_authenticated:
        return redirect("/")
        
    return render(request, 'account/login_wave.html',context)


def log_out(request):
    logout(request)
    return redirect("/")

@login_required(login_url='/login')
def user_account(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    books = Book.objects.filter(user=user)
    profile = user_profile.objects.filter(user=request.user).first()
    editForm = editRegisterForm(request.POST or None, request.FILES or None,
    initial={
        'user_name':user.username, 
        'email':user.email,
        'profile_pic':profile.profile_pic,
        'city':profile.city,
        'address':profile.address,
        'gender':profile.gender,
        'phone_num':profile.phone_num,
        'whatsapp_num':profile.whatsapp_num,
        })
    if editForm.is_valid():
        profile_pic = editForm.cleaned_data.get('profile_pic')
        user_name = editForm.cleaned_data.get('user_name')
        email = editForm.cleaned_data.get('email')
        city = editForm.cleaned_data.get('city')
        address = editForm.cleaned_data.get('address')
        gender = editForm.cleaned_data.get('gender')
        phone_num = editForm.cleaned_data.get('phone_num')
        whatsapp_num = editForm.cleaned_data.get('whatsapp_num')
        username_is_exist = User.objects.filter(username=user_name).exists()
        email_is_exist = User.objects.filter(email=email).exists()
        if username_is_exist:
            if user.username == user_name:
                pass
            else:
                messages.error(request, "The username already exists")   
        else:
            user.username = user_name

        if email_is_exist:
            if user.email == email:
                pass
            else:
                messages.warning(request, "The email already exists")   
        else:
            user.email = email

        user.user_profile.city = city
        user.user_profile.address = address
        user.user_profile.gender = gender
        user.user_profile.phone_num = phone_num
        user.user_profile.whatsapp_num = whatsapp_num
        user.user_profile.profile_pic = profile_pic
        user.save()
        user.user_profile.save()
        
    context = {
            'editForm' : editForm,
            'books' : books,
        }

    return render(request, './user_account.html', context)
    
@login_required(login_url='/login')
def myBooks(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    books = Book.objects.filter(user=user)
    return render(request, './my_books.html', {'books':books})


@login_required(login_url='/login')
def remove_my_book(request, *args, **kwargs):
    book_id = kwargs.get('detail_id')
    if book_id is not None:
        book_detail = Book.objects.get_queryset().get(id=book_id)
        if book_detail is not None:
            book_detail.delete()
    return redirect('/my-books')



@login_required(login_url='/login')
def edit_my_book(request, *args, **kwargs):
    book_id = kwargs.get('detail_id')
    if book_id is not None:
        book_detail = Book.objects.get_queryset().get(id=book_id)
        if book_detail is not None:
            editBook = sellBookForm(request.POST or None, request.FILES or None, 
            initial={
                'book_name':book_detail.title,
                'book_author':book_detail.Author,
                'book_publisher':book_detail.publisher,
                'book_edition':book_detail.edition,
                'book_language':book_detail.language,
                'price':book_detail.price,
                'date':book_detail.Date,
                'category':[i.id for i in book_detail.category.all()],
                'description':book_detail.description,
                'book_pic':book_detail.image,
            })

            if editBook.is_valid():

                bookName = editBook.cleaned_data.get('book_name')
                book_author = editBook.cleaned_data.get('book_author')
                book_publisher = editBook.cleaned_data.get('book_publisher')
                book_edition = editBook.cleaned_data.get('book_edition')
                book_language = editBook.cleaned_data.get('book_language')
                price = editBook.cleaned_data.get('price')
                category = editBook.cleaned_data.get('category')
                book_pic = editBook.cleaned_data.get('book_pic')
                date = editBook.cleaned_data.get('date')
                description = editBook.cleaned_data.get('description')

                book_detail.title=bookName
                book_detail.Author=book_author
                book_detail.publisher=book_publisher
                book_detail.edition=book_edition
                book_detail.price=price
                book_detail.language=book_language
                book_detail.Date=date
                book_detail.category.set(category)
                book_detail.description=description
                book_detail.image=book_pic

                book_detail.save()

    context = {
            'editBook' : editBook,
            'bookDetail':book_detail,
        }

    return render(request, './editBook.html', context)