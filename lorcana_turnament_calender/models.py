from django.db import models

# Create your models here.

class Event(models.Model):
    COLOR_CHOICES = [
        ("red", "Rot"),
        ("blue", "Blau"),
        ("green", "Grün"),
        ("orange", "Orange"),
    ]

    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=25, default='Turnament')
    location_name = models.CharField(max_length=35, default='---')
    location_plz = models.IntegerField(default=0)
    location_city = models.CharField(max_length=200, default='---')
    link = models.URLField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='orange')

    def __str__(self):
        return self.title + " @ " + self.location_name + " (" + self.start.strftime("%d.%m.%Y") + ")"