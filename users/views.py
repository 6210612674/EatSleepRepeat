from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import CreateView
from .form import CustomerSignUpForm, StoreSignUpForm, UpdateCustomerForm, UpdateStoreForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Customer, Store


# Create your views here.

class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/users/customer_register.html'

    def form_valid(self, form):
        user = form.save()
        return redirect('/users/login')


class store_register(CreateView):
    model = User
    form_class = StoreSignUpForm
    template_name = '../templates/users/store_register.html'

    def form_valid(self, form):
        user = form.save()
        return redirect('/users/login')


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


def favourite(request, store_user):
    user = User.objects.get(username=request.user.username)
    store = Store.objects.get(user=store_user)
    if request.user in store.favourite.all():
        store.favourite.remove(user)
    else:
        store.favourite.add(user)
    return redirect("homepage:index")


def favourite_view(request, customer_user):
    user = User.objects.get(username=request.user.username)

    return render(request, "users/favourite_view.html", {
        "stores": Store.objects.filter(favourite=user),
        })



# def favorite_viewview(request, id):
#     post =Store.objects.all();
#     if post.favorite.filter(id=request.user.id).exists():

#     else:
#         post.favorite.add(request.user)
#     return redirect('article_detail', pk=article.pk)


"""
def favourite_view(request):
    fav_list = []
    for f in Store.objects.all():
        if request.user in c.favourite.all():
        fav_list.append(c)
    return render(request, "users/favourite_view.html",{
        "fav_list" : fav_list,
    })

 "stores": Store.favourite.objects.filter(User,customer)

store = store_user
    return render(request, "storepage/storeitem.html",{
        "store": store,
        "foods": Food.objects.filter(registered_store=store)
    })
"""

def customer_profile(request):
    if request.method == 'POST':
        user_form = UpdateCustomerForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('users:customer')
    else:
        user_form = UpdateCustomerForm(instance=request.user)

    return render(request, 'users/customer_profile.html', {
        'user_form': user_form,
    })


def store_profile(request):
    if request.method == 'POST':
        user_form = UpdateStoreForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('users:store')
    else:
        user_form = UpdateStoreForm(instance=request.user)

    return render(request, 'users/store_profile.html', {
        'user_form': user_form,
    })