from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='index'),
    path('EatSleepRepeat_report/', views.report, name='report'),
    ]