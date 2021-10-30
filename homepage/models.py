from django.db import models
from users.models import User, Store
from django.utils import timezone


# Create your models here.
class Food (models.Model):
    class Category(models.IntegerChoices):
        MainCourse = 1
        Appetizer = 2
        Dessert = 3
        Drink = 4

    active = models.BooleanField(default=True)
    F_id = models.AutoField(primary_key=True)
    F_name = models.CharField(max_length=150)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    description = models.CharField(max_length=150)
    category = models.IntegerField(choices = Category.choices)
    registered_store = models.ManyToManyField(User, blank=True, related_name="regisstore")

    def __str__(self):
        return  f"{self.F_id} : {self.F_name}: {self.price}: {self.description}: {self.category}:"

class Order (models.Model):

    O_id = models.CharField(max_length=30)
    '''date = models.DateTimeField(default=timezone.now(), blank=True)
    time = timezone.now()'''
    amount = models.DecimalField(max_digits=20, decimal_places=2,)


    def __str__(self):
        return  f"{self.id} {self.O_id} : {self.amount}"


class Payment (models.Model):
    class PaymentOptions(models.IntegerChoices):
        cash = 1
        ecommerce = 2

    class Pickup(models.IntegerChoices):
        pick_up = 1
        delivery = 2

    P_id = models.CharField(max_length=30)
    paymentOptions = models.IntegerField(choices = PaymentOptions.choices)
    pickup = models.IntegerField(choices = Pickup.choices)

    def __str__(self):
        return  f"{self.id} {self.P_id} : {self.paymentOptions} : {self.pickup} :"

