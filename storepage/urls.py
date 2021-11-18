from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="storepage"

urlpatterns = [
    path('addfoodview/',views.addfood_view, name='addfoodview'),
    path('statistic/',views.statistic_view, name='statistic'),
    path('comment/', views.addcomment , name='addcomment'),
    path('addfood/', views.addfood , name='addfood'),
    path('<int:F_id>/edit/', views.edit , name='edit'),
    path('<str:store_user>/',views.storeitem, name='storeitem'),
    path('<int:F_id>/remove/', views.remove , name='remove'),
    path('<int:F_id>/editview/', views.edit_view , name='edit_view'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)