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

def events_api(request):
    events = Event.objects.all()

    data = []
    for e in events:
        data.append({
            "id": e.id,
            "title": e.title,
            "start": e.start.isoformat(),
            "end": e.end.isoformat() if e.end else None,
        })

    return JsonResponse(data, safe=False)

def event_detail_api(request, pk):
    e = Event.objects.get(pk=pk)

    return JsonResponse({
        "id": e.id,
        "title": e.title,
        "link": e.link,
        "image": e.image.url if e.image else None,
        "start": e.start.isoformat(),
        "end": e.end.isoformat() if e.end else None,
    })