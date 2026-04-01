from django.http import HttpResponse
from django.shortcuts import render
from .models import CalenderEntry

# Create your views here.
def home(request):
    return render(request,'home.html')

def calender(request):
    calender_entries = CalenderEntry.objects.all()
    return render(request,'calender.html', {"entries": calender_entries})