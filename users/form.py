from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Customer,Store

class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    tel = forms.CharField(required=True)
    sex = forms.CharField(required=True)
    address = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.tel = self.cleaned_data.get('tel')
        user.sex = self.cleaned_data.get('sex')
        user.email = self.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.address=self.cleaned_data.get('address')
        customer.save()
        return user

class StoreSignUpForm(UserCreationForm):
    store_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    tel = forms.CharField(required=True)
    sex = forms.CharField(required=True)
    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_store = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.tel = self.cleaned_data.get('tel')
        user.sex = self.cleaned_data.get('sex')
        user.email = self.cleaned_data.get('email')
        user.save()
        store = Store.objects.create(user=user)
        store.location=self.cleaned_data.get('location')
        store.store_name=self.cleaned_data.get('store_name')
        store.save()
        return user

'''
class StoreAddFood(forms.Form):
    product_name = form.CharField(
        label = '',
        required = False,
        max_length = 30,
        min_length = 2,
        widget = forms.TextInput(attrs={
            'placeholder': 'Food Name',
            'size': '30'
        })
    )

    product_price = form.CharField(
    label = '',
    required = False,
    widget = forms.TextInput(attrs={
        'placeholder': 'Price',
        'size': '10'
    })
)

'''