from django.db import models

# Create your models here.


class contactUs(models.Model):

    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    is_read = models.BooleanField()


    def __str__(self):
        return self.subject