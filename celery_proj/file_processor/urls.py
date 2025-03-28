from django.urls import path
from . import views
urlpatterns = [
    path('upload/', views.FileUploadView.as_view(), name='file-upload'),
    path('status/<int:file_id>', views.FileStatusView.as_view(), name='file-status'),
    path('test/', views.SumView.as_view())
]