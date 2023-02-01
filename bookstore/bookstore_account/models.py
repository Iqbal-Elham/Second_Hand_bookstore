from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import os

# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.user.username}{ext}"
    return f"users/{final_name}"


class user_profile(models.Model):
  user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
  city = models.CharField(max_length=100, blank=True, null=True)
  address = models.CharField(max_length=500, blank=True, null=True)
  gender = models.CharField(max_length=10,default='Male')
  phone_num = models.CharField(max_length=15, blank=True, null=True)
  whatsapp_num = models.CharField(max_length=15, blank=True, null=True)
  profile_pic = models.ImageField(default='default.jpg', upload_to=upload_image_path)
  

  def __str__(self):
    return str(self.user.username)

