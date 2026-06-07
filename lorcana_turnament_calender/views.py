from django.shortcuts import render
from .models import Event, Question, Player
from .forms import ContactForm
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string


# Create your views here.
def home(request):
    latest_player = Player.objects.order_by("-qualification_date").first()

    cutoff = timezone.now()

    next_event = Event.objects.filter(
        date__gte=cutoff
    ).order_by("date").first()
    return render(request,'home.html', {
        'latest_player': latest_player,
        'next_event': next_event
    })

def qualified(request):
    players = Player.objects.order_by("-qualification_date")
    return render(request,'qualified.html', {
        'players': players
    })

def calender(request):
    cutoff = timezone.now() - timedelta(days=2)

    calender_entries = Event.objects.filter(
        date__gte=cutoff
    ).order_by("date")

    return render(request, "calender.html", {
        "entries": calender_entries
    })

def about(request):
    questions = Question.objects.all().order_by("-ranking")
    return render(request,'about.html', {
        'questions': questions
    })

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            eventlocation = form.cleaned_data['eventlocation']
            permit = form.cleaned_data['permit']
            capacity = form.cleaned_data['capacity']
            experience = form.cleaned_data['experience']
            name = form.cleaned_data["name"]
            email = form.cleaned_data['email']
            notes = form.cleaned_data['notes']

            html = render_to_string('contactform.html', {
                'name': name,
                'email': email,
                'city': city,
                'eventlocation': eventlocation,
                'capacity': capacity,
                'permit': permit,
                'experience': experience,
                'notes': notes
            })

            subject = "Turnier-Bewerbung von " + name + " @ " + eventlocation + " in " + city

            send_mail(subject=subject,from_email= email, html_message=html)

    else:
        form = ContactForm()

    return render(request,'contact.html', {
        'form': form
    })
