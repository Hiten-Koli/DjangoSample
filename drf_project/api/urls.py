from . import views
from django.urls import path

urlpatterns = [
    path('students/', views.studentView),
]