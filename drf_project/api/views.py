from django.shortcuts import get_object_or_404
# from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer, EmployeeSerializer, CustomerSerializer, BlogSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from customers.models import Customer
from rest_framework import status, mixins, generics, viewsets
from blogs.models import Blog, Comment
from .paginations import CustomPagination
from customers.filters import CustomerFilter
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
@api_view(['GET','POST'])
def studentView(request):
     if request.method=="GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True )
        return Response(serializer.data, status=status.HTTP_200_OK)
     elif request.method == 'POST':
         serializer = StudentSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         print(serializer.errors)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
@api_view(['GET','PUT','DELETE'])    
def studentSpecificView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except student.DoesNotExists:
        return Response( status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Employees(APIView):
    def get(self, request):
        employees= Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class employeeSpecificView(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''  Mixins

class Customers(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
    
class SpecificCustomer(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    def put(self, request, pk):
        return self.update(request, pk)
    def delete(self, request, pk):
        return self.destroy(request, pk)
'''
'''
#Generics
# class Customers(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
class Customers(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# class SpecificCustomer(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#     lookup_field = 'pk'

class SpecificCustomer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'pk'

'''
'''Viewset
class CustomersViewset(viewsets.ViewSet):
    def list(self, request):
        queryset= Customer.objects.all()
        serializer = CustomerSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        customer = get_object_or_404(Customer, pk=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk=None):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return Response( status=status.HTTP_204_NO_CONTENT)
'''
class CustomersViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomPagination
    # filterset_fields = ['age']
    filterset_class = CustomerFilter


class BlogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['^title', 'body']
    ordering_fields = ['id', 'title']

class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogsSpecificView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentsSpecificView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'