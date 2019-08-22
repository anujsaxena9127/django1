from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name="shophome"),
    path('about/', views.about,name="shophome"),
    path('contact/', views.contact,name="shophome"),
    path('tracker/', views.tracker,name="shophome"),
    path('search/', views.search,name="shophome"),
    path('', views.index,name="shophome"),
    path('', views.index,name="shophome"),
    path('', views.index,name="shophome"),
    path('', views.index,name="shophome"),
]
