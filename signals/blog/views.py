from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
# Create your views here.
def currtime(request):
    current_time = timezone.now().strftime('%H:%M:%S')
    return HttpResponse(current_time)