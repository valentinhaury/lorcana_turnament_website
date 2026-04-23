from django.db import models

# Create your models here.

class Event(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200, default='---')
    location_plz = models.IntegerField(default=0)
    location_city = models.CharField(max_length=200, default='---')
    link = models.TextField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)