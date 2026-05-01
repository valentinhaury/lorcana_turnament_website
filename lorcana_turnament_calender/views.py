from django.shortcuts import render
from .models import Event
from datetime import timedelta
from django.utils import timezone


# Create your views here.
def home(request):
    return render(request,'home.html')


def calender(request):
    cutoff = timezone.now() - timedelta(days=2)

    calender_entries = Event.objects.filter(
        start__gte=cutoff
    ).order_by("start")

    return render(request, "calender.html", {
        "entries": calender_entries
    })

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
