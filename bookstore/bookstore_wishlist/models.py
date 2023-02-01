from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from bookstore_products.models import Book

class Wish(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.owner.get_username()

class wishDetail(models.Model):
    wish = models.ForeignKey(Wish, on_delete=models.CASCADE)
    wishBook = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.IntegerField()


    def __str__(self):
        return self.wishBook.title
