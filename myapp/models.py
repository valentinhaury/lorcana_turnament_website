from django.db import models

# Create your models here.

class CalenderEntry(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    #picture = models.ImageField(upload_to='images/')