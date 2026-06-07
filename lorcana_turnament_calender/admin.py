from django.contrib import admin
from .models import Event, Question, Player

# Register your models here.
admin.site.register(Event)
admin.site.register(Question)
admin.site.register(Player)