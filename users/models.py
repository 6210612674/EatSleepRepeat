from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_store = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    address = models.CharField(max_length=100)

class Store(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    location = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100,default="0")