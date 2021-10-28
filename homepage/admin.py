from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.

from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ("O_id", "amount")


class FoodAdmin(admin.ModelAdmin):
    list_display = ("active", "F_id", "F_name", "price", "category")


class PaymentAdmin(admin.ModelAdmin):
    list_display = ("P_id", "paymentOptions", "pickup")


admin.site.register(Order, OrderAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Payment, PaymentAdmin)


