from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=200)
    ranking = models.IntegerField(default=0)

    def __str__(self):
        return str(self.ranking)

class Event(models.Model):
    COLOR_CHOICES = [
        ("red", "Rot"),
        ("blue", "Blau"),
        ("green", "Grün"),
        ("orange", "Orange"),
    ]

    date = models.DateTimeField()
    registration_end = models.DateTimeField()
    title = models.CharField(max_length=25, default='Turnament')
    location_plz = models.IntegerField(default=0)
    location_city = models.CharField(max_length=200, default='---')
    link = models.URLField()
    maps = models.URLField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='orange')

    def __str__(self):
        return self.title + " " + self.date.strftime("%d.%m.%Y")