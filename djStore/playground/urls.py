from django.urls import path
from . import views
#UrlConfig
urlpatterns = [
    path('hello/', views.say_hello),
    path('about/', views.about),
    path('services/', views.services),
    path('contact/', views.contact),
    path('index/', views.index),
]