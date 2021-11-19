from django.shortcuts import render ,redirect
from django.http import HttpResponse
from users.models import User, Store , Customer

# Create your views here.

def index(request):
    return render(request, "homepage/index.html", {
        "stores": Store.objects.all(),
    })


def googlemap(request):
    return render(request, "homepage/googlemap.html")


def layout(request):
    return render(request, "homepage/layout.html", {
        "stores": Store.objects.all(),
        "customers": Customer.objects.all(),
    })


def store_search(request):
    if 'search' in request.GET:
        search_term = request.GET['search']
        stores = Store.objects.all().filter(store_name=search_term)

    return render(request, 'homepage/search.html',{
        "store": stores,
    })


def store_search_place(request):
    if 'search' in request.GET:
        search_term = request.GET['search']
        stores2 = Store.objects.all().filter(place=search_term)

    return render(request, 'homepage/search_place.html',{
        "store": stores2,
    })