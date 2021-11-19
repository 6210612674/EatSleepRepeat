from django.urls import path
from . import views

app_name = "homepage"

urlpatterns = [
    path('', views.index, name='index'),
    path('googlemap', views.googlemap, name='googlemap'),
    path('layout', views.layout, name='layout'),
    path('search', views.store_search, name='search'),
    path('search_place', views.store_search_place, name='store_search_place')
]