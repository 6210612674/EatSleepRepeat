from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Customer, Store

class CustomerSignUpForm(UserCreationForm):

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
        ('I prefer not to say', 'I prefer not to say'),
    ]

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    tel = forms.CharField(required=True)
    gender = forms.ChoiceField(choices = GENDER, required=True)
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
        user.gender = self.cleaned_data.get('gender')
        user.email = self.cleaned_data.get('email')
        user.save()
        customer = Customer.objects.create(user=user)
        customer.address = self.cleaned_data.get('address')
        customer.save()
        return user

class StoreSignUpForm(UserCreationForm):

    TYPE = [
        ('Coffee', 'Coffee'),
        ('Bubble Tea', 'Bubble Tea'),
        ('Streetfood', 'Streetfood'),
        ('A la cart', 'A la cart'),
        ('Noodle', 'Noodle'),
        ('Buffet', 'Buffet'),
        ('Shabu', 'Shabu'),
        ('Grill', 'Grill'),
        ('Bakery', 'Bakery'),
        ('Dessert', 'Dessert'),
        ('Cafe', 'Cafe'),
        ('Boiled rice', 'Boiled rice'),
        ('Karaoke', 'Karaoke'),
        ('Wine', 'Wine'),
        ('Clean-food', 'Clean-food'),
        ('Fastfood','Fastfood'),
        ('Seafood', 'Seafood'),
        ('Louge', 'Louge'),
        ('Japanese', 'Japanese'),
        ('Thai', 'Thai'),
        ('Korean', 'Korean'),
        ('Indian', 'Indian'),
        ('American','American'),
        ('Italian','Italine'),
        ('Vietnamese', 'Vietnamese'),
    ]

    PLACE = [
        ('Chiang Rak 1', 'Chiang Rak 1'),
        ('Chiang Rak 2', 'Chiang Rak 2'),
        ('Twin Town', 'Twin Town'),
        ('TU Dome', 'TU Dome'),
        ('Green Canteen', 'Green Canteen'),
        ('Golf View', 'Golf View'),
        ('Tiw Son Dome', 'Tiw Son Dome'),
        ('J-Park', 'J-Park'),
        ('JC canteen', 'JC canteen'),
        ('SC canteen', 'SC canteen'),
        ('opposite Chiang Rak', 'opposite Chiang Rak'),
    ]

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
        ('I prefer not to say', 'I prefer not to say'),
    ]

    store_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField()
    tel = forms.CharField(required=True)
    gender = forms.ChoiceField(choices = GENDER, required=True)
    location = forms.CharField(required=True)
    type_store = forms.ChoiceField(choices = TYPE, required=True)
    place = forms.ChoiceField(choices = PLACE, required=True)
    location_url = forms.CharField(required=True)
    store_image = forms.ImageField()

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
        user.gender = self.cleaned_data.get('gender')
        user.email = self.cleaned_data.get('email')
        user.save()
        store = Store.objects.create(user=user)
        store.location = self.cleaned_data.get('location')
        store.store_name = self.cleaned_data.get('store_name')
        store.type_store = self.cleaned_data.get('type_store')
        store.place = self.cleaned_data.get('place')
        store.location_url = self.cleaned_data.get('location_url')
        store.store_image = self.cleaned_data.get('store_image')
        store.save()
        return user

class UpdateCustomerForm(forms.ModelForm):

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
        ('I prefer not to say', 'I prefer not to say'),
    ]

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    tel = forms.CharField()
    gender = forms.ChoiceField(choices = GENDER)
    address = forms.CharField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'tel', 'gender', 'address']


class UpdateStoreForm(forms.ModelForm):

    TYPE = [
        ('Coffee', 'Coffee'),
        ('Bubble Tea', 'Bubble Tea'),
        ('Streetfood', 'Streetfood'),
        ('A la cart', 'A la cart'),
        ('Noodle', 'Noodle'),
        ('Buffet', 'Buffet'),
        ('Shabu', 'Shabu'),
        ('Grill', 'Grill'),
        ('Bakery', 'Bakery'),
        ('Dessert', 'Dessert'),
        ('Cafe', 'Cafe'),
        ('Boiled rice', 'Boiled rice'),
        ('Karaoke', 'Karaoke'),
        ('Wine', 'Wine'),
        ('Clean-food', 'Clean-food'),
        ('Fastfood','Fastfood'),
        ('Seafood', 'Seafood'),
        ('Louge', 'Louge'),
        ('Japanese', 'Japanese'),
        ('Thai', 'Thai'),
        ('Korean', 'Korean'),
        ('Indian', 'Indian'),
        ('American','American'),
        ('Italian','Italine'),
        ('Vietnamese', 'Vietnamese'),
    ]

    PLACE = [
        ('Chiang Rak 1', 'Chiang Rak 1'),
        ('Chiang Rak 2', 'Chiang Rak 2'),
        ('Twin Town', 'Twin Town'),
        ('TU Dome', 'TU Dome'),
        ('Green Canteen', 'Green Canteen'),
        ('Golf View', 'Golf View'),
        ('Tiw Son Dome', 'Tiw Son Dome'),
        ('J-Park', 'J-Park'),
        ('JC canteen', 'JC canteen'),
        ('SC canteen', 'SC canteen'),
        ('opposite Chiang Rak', 'opposite Chiang Rak'),
    ]

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
        ('I prefer not to say', 'I prefer not to say'),
    ]

    store_name = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    tel = forms.CharField()
    gender = forms.ChoiceField(choices = GENDER)
    location = forms.CharField()
    type_store = forms.ChoiceField(choices = TYPE)
    place = forms.ChoiceField(choices = PLACE)
    location_url = forms.CharField()

    class Meta:
        model = User
        fields = ['store_name', 'first_name', 'last_name', 'email', 'tel', 'gender', 'location', 'type_store', 'place', 'location_url']

