from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("calender/", views.calender, name="calender"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("api/events/", views.events_api),
    path("api/events/<int:pk>/", views.event_detail_api),
]