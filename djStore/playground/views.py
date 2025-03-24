from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from playground.models import Contact
from django.contrib import messages
# Create your views here.
def say_hello(request):
    return render(request, 'hello.html', {'name': 'Hiten'})

def about(request):
   # return HttpResponse('This is about Page')
   return render(request, 'about.html')
def services(request):
   # return HttpResponse('This is services Page')
   return render(request, 'services.html')
def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        message= request.POST.get('message')
        contact = Contact(name=name, email=email, message=message, date =datetime.today())
        contact.save()
        messages.success(request, "Message sent Successfully!!")
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')