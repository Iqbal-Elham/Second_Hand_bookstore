from django.db import models

# Create your models here.

class bookCategory(models.Model):
    title = models.CharField(max_length = 150)


    def __str__(self):
        return self.title