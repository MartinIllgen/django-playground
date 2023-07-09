from django.contrib import admin

from .models import Participant, Event

admin.site.register(Event)
admin.site.register(Participant)