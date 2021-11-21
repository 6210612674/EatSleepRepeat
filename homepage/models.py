from django.db import models
from users.models import User, Store
from django.utils.timezone import now
from datetime import datetime


# Create your models here.
class Food (models.Model):

    CATEGORY = [
        ('Main', 'Main'),
        ('Appetizer', 'Appetizer'),
        ('Dessert', 'Dessert'),
        ('Drink', 'Drink'),
    ]

    active = models.BooleanField(default=True)
    F_id = models.AutoField(primary_key=True)
    F_name = models.CharField(max_length=150)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    description = models.CharField(max_length=150)
    category = models.CharField(max_length=100 ,choices = CATEGORY)
    registered_store = models.ManyToManyField(User, blank=True, related_name="regisstore")
    food_image = models.ImageField(upload_to='static/foodimg/', blank = True)

    def __str__(self):
        return  f"{self.F_id} {self.F_name} {self.price} {self.description} {self.category}"

class Comment (models.Model):

    commented_store = models.ManyToManyField(User, blank=True, related_name="comstore")
    comment_name = models.CharField(max_length=300)
    comment_text = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return  f"{self.commented_store} : {self.comment_name}  {self.comment_text}"