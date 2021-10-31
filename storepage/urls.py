from django.urls import path
from . import views

app_name="storepage"

urlpatterns = [
    path('addfoodview/',views.addfood_view, name='addfoodview'),
    path('statistic/',views.statistic_view, name='statistic'),
    path('addfood/', views.addfood , name='addfood'),
    path('<str:store_user>/',views.storeitem, name='storeitem'),

]