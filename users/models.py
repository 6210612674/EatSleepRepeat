from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.storage import FileSystemStorage

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_store = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    address = models.CharField(max_length=100)

class Store(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    location = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100, default="0")
    type_store  = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    location_url = models.CharField(max_length=100)
    store_image = models.ImageField(upload_to='media/storeimg/', blank = True)
    favourite = models.ManyToManyField(User ,related_name = 'favourite',blank = True)
