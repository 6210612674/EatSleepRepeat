from django.shortcuts import render
from users.models import User, Store, Customer
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from homepage.models import *
from django.db.models import Avg



# Create your views here.

@login_required(login_url='users:login')
def addfood_view(request):
    user = User.objects.get(username=request.user.username)
    return render(request, "storepage/addfood.html",{
        "foods": Food.objects.filter(registered_store=user)
    })


@login_required(login_url='users:login')
def statistic_view(request):
    user = User.objects.get(username=request.user.username)
    counter = Comment.objects.filter(commented_store=user).count()
    viewcount = user.view_count
    foods= Food.objects.filter(registered_store=user).count()
    com = Comment.objects.filter(commented_store=user)
    avg = Comment.objects.filter(commented_store=user).aggregate(Avg('rating'))['rating__avg']
    store = Store.objects.get(user=request.user.id)
    tfav = store.favourite.count()

    return render(request, "storepage/statistic.html",{
        "stores": viewcount,
        "count": counter,
        "foods" : foods,
        "com": com,
        "avg" : avg,
        "tfav" : tfav,
    })


def storeitem(request, store_user):
    store = store_user
    store2 = User.objects.get(id=store)
    store2.view_count += 1
    store2.save()
    return render(request, "storepage/storeitem.html",{
        "store": store,
        "foods": Food.objects.filter(registered_store=store),
        "stores": Store.objects.filter(user=store),
        "comments": Comment.objects.filter(commented_store=store)
    })


@login_required(login_url='users:login')
def addcomment(request):

    if request.method == "POST":
        comuser = request.POST.get("user")
        userstore = User.objects.get(username=comuser)
        comment = Comment.objects.create(
            comment_name = request.POST.get("name"),
            comment_text = request.POST.get("review"),
            rating = request.POST.get("rate"),
        )

        comment.commented_store.add(userstore)
        comment.save()
    return render(request, "storepage/ThankyouC.html")


@login_required(login_url='users:login')
def addfood(request):
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        food = Food.objects.create(
            F_name = request.POST['foodname'],
            price = request.POST['price'],
            category = request.POST['type'],
            description = request.POST['description'],
            food_image = request.FILES['foodimage'],
        )

        food.registered_store.add(user)
        food.save()
    return HttpResponseRedirect(reverse("storepage:addfoodview"))


@login_required(login_url='users:login')
def remove(request, F_id):
    Food.objects.filter(F_id=F_id).delete()

    return HttpResponseRedirect(reverse("storepage:addfoodview"))


@login_required(login_url='users:login')
def edit(request, F_id):
    food = Food.objects.get(F_id = F_id)
    if request.method == "POST":
        food.F_name = request.POST['foodname']
        food.price = request.POST['price']
        food.category = request.POST['type']
        food.description = request.POST['description']
        food.food_image = request.FILES['foodimage']
        food.save()

    return HttpResponseRedirect(reverse("storepage:addfoodview"))


@login_required(login_url='users:login')
def edit_view(request, F_id):
    return render(request, "storepage/editview.html",{
        "foods": Food.objects.filter(F_id=F_id),
    })
