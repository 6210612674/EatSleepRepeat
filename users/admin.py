from django.contrib import admin
from .models import User, Customer, Store

# Register your models here.

class StoreAdmin(admin.ModelAdmin):
    list_display = ("user", "store_name", "verify")

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user",)

admin.site.register(User)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Store, StoreAdmin)