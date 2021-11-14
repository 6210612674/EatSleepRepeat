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