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
    view_count = models.IntegerField(default=0)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    address = models.CharField(max_length=100)

class Store(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    location = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100, default="0")
    type_store  = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    location_url = models.CharField(max_length=100)
    store_image = models.ImageField(upload_to='static/storeimg/', blank=True)
    favourite = models.ManyToManyField(User , related_name='favourite', blank=True)
    description = models.CharField(max_length=1000, blank=True)
    verify = models.BooleanField(default=False)
    open_time = models.TimeField(max_length=100, blank=True, null=True)
    close_time = models.TimeField(max_length=100, blank=True, null=True)
    delivery_link = models.URLField(max_length=1000, blank=True)
    status = models.CharField(max_length=100)

