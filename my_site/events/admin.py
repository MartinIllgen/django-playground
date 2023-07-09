from django.contrib import admin

from .models import Participant, Event

class ParticipantAdmin(admin.ModelAdmin):
  list_display = ["surname", "given_name", "email", "participates", "has_payed"]
  
class EventAdmin(admin.ModelAdmin):
  list_display = ["start_date", "name"]

admin.site.register(Event, EventAdmin)
admin.site.register(Participant, ParticipantAdmin)