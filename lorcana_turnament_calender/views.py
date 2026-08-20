from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Event, Question, Player
from .forms import ContactForm
from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


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
    latest_player = Player.objects.order_by("-qualification_date").first()

    cutoff = timezone.now()

    next_event = Event.objects.filter(
        date__gte=cutoff
    ).order_by("date").first()
    players = Player.objects.order_by("-qualification_date")
    return render(request,'qualified.html', {
        'players': players,
        'latest_player': latest_player,
        'next_event': next_event
    })

def calender(request):
    latest_player = Player.objects.order_by("-qualification_date").first()

    cutoff = timezone.now()

    next_event = Event.objects.filter(
        date__gte=cutoff
    ).order_by("date").first()

    cutoff = timezone.now() - timedelta(days=2)

    calender_entries = Event.objects.filter(
        date__gte=cutoff
    ).order_by("date")

    return render(request, "calender.html", {
        "entries": calender_entries,
        'latest_player': latest_player,
        'next_event': next_event
    })

def about(request):
    latest_player = Player.objects.order_by("-qualification_date").first()

    cutoff = timezone.now()

    next_event = Event.objects.filter(
        date__gte=cutoff
    ).order_by("date").first()

    questions = Question.objects.all().order_by("-ranking")
    return render(request,'about.html', {
        'questions': questions,
        'latest_player': latest_player,
        'next_event': next_event
    })
@ensure_csrf_cookie
def contact(request):
    latest_player = Player.objects.order_by("-qualification_date").first()

    cutoff = timezone.now()

    next_event = Event.objects.filter(
        date__gte=cutoff
    ).order_by("date").first()


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

            send_mail(
                subject=subject,
                from_email= settings.EMAIL_HOST_USER,
                message=html,
                recipient_list=['legendzadmin@gmail.com']
            )

            messages.success(
                request,
                "Die Bewerbung wurde erfolgreich übermittelt."
            )

            return redirect('contact')

    else:
        form = ContactForm()

    return render(request,'contact.html', {
        'form': form,
        'latest_player': latest_player,
        'next_event': next_event
    })
