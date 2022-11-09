from django.db import models
from django.db.models import Q
import os

# Create your models here.


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"products/{final_name}"

class productManager(models.Manager):

    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_by_id(self, book_id):
        qs = self.get_queryset().filter(id=book_id)
        
        if qs.count() == 1 :
            return qs.first()
        return None

    def search(self,query):
        lookup = Q(title__icontains = query) | Q(description__icontains = query) | Q(Author__icontains = query)
        return self.get_queryset().filter(lookup, active = True).distinct()


class book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    Author = models.CharField(max_length=150, null=True)
    publisher = models.CharField(max_length=150, null=True)
    Date = models.DateTimeField(null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    active = models.BooleanField(default=False)

    objects = productManager()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f'/books/{self.id}/{self.title.replace(" ", "-")}'
