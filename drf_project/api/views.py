# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def studentView(request):
     if request.method=="GET":
        students = Student.objects.all()
        serialize = StudentSerializer(students, many=True )
        return Response(serialize.data, status=status.HTTP_200_OK)