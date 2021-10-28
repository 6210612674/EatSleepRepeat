from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import CreateView
from .form import CustomerSignUpForm, StoreSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User

# Create your views here.

def register(request):
    return render(request, '../templates/users/register.html')

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/users/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class store_register(CreateView):
    model = User
    form_class = StoreSignUpForm
    template_name = '../templates/users/store_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return HttpResponseRedirect(reverse("homepage:index"))
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/users/login.html',

    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect("homepage:index")


def customer_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

    return render(request, "users/customer_account.html")



def store_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))

    return render(request, "users/store_account.html")

