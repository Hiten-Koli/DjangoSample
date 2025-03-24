from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def students(request):
    student =[{"id":1, "name":"TestName1", "age":23}]
    return HttpResponse(student)