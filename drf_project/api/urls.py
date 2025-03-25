from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('customers',views.CustomersViewset, basename = 'customer' )

urlpatterns = [
    path('students/', views.studentView),
    path('students/<int:pk>', views.studentSpecificView),
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>', views.employeeSpecificView.as_view()),
    # path('customers/', views.Customers.as_view()),
    # path('customers/<int:pk>', views.SpecificCustomer.as_view()),
    path('', include(router.urls)),
    path('blogs/', views.BlogsView.as_view()),
    path('blogs/<int:pk>', views.BlogsSpecificView.as_view()),
    path('comments/', views.CommentsView.as_view()),
    path('comments/<int:pk>', views.CommentsSpecificView.as_view()),
]