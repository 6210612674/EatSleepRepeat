from django.urls import path, re_path
from . import views

app_name="users"

urlpatterns = [
    path('register/customer_register/',views.customer_register.as_view(), name='customer_register'),
    path('register/store_register/',views.store_register.as_view(), name='store_register'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('customer/',views.customer_view, name='customer'),
    path('store/',views.store_view, name='store'),
    path('favourite/<str:store_user>', views.favourite, name='favourite'),


]