from django.shortcuts import render
from .models import Event
from .forms import ContactForm
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail


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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data['email']
            eventlocation = form.cleaned_data['eventlocation']
            city = form.cleaned_data['city']
            date = form.cleaned_data['date']
            content = form.cleaned_data['content']

            subject = "Turnier-Bewerbung von " + eventlocation + " am " + str(date)
            message = "Name: " + name + ". TurnierBewerbung von " + eventlocation + " am " + str(date) + " in " + city + " Nachricht: " + content

            send_mail(subject, message, email, ['valentinhaury@gmai.com'])

    else:
        form = ContactForm()

    return render(request,'contact.html', {
        'form': form
    })
