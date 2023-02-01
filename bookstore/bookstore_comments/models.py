from django.db import models
from django.contrib.auth.models import User
from bookstore_products.models import Book
# Create your models here.

class Comments(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE,)
  book = models.ForeignKey(Book, on_delete=models.CASCADE,)
  comment = models.TextField()
  date = models.DateTimeField(null=True)

  def __str__(self):
        return str(self.user.username)
