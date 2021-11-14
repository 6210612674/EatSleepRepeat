from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="users"

urlpatterns = [
    path('register/customer_register', views.customer_register.as_view(), name='customer_register'),
    path('register/store_register', views.store_register.as_view(), name='store_register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('customer', views.customer_view, name='customer'),
    path('store',views.store_view, name='store'),
    path('favourite/<str:store_user>', views.favourite, name='favourite'),
    path('favourite_view/<str:customer_user>', views.favourite_view, name='favourite_view'),
    path('customer_profile', views.customer_profile, name='customer_profile'),
    path('store_profile', views.store_profile, name='store_profile'),
]

