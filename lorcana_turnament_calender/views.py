from django.http import JsonResponse
from django.shortcuts import render
from .models import Event

# Create your views here.
def home(request):
    return render(request,'home.html')

def calender(request):
    calender_entries = Event.objects.all()
    return render(request,'calender.html', {"entries": calender_entries})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
