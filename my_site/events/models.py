from django.db import models

class Event(models.Model):
  name = models.CharField(max_length=255)
  start_date = models.DateTimeField()
    
class Participant(models.Model):
  given_name = models.CharField(max_length=255)
  surname = models.CharField(max_length=255)
  email = models.CharField(max_length=255, primary_key=True, unique=True)
  event = models.ForeignKey("Event", on_delete=models.CASCADE, )
  password = models.CharField(max_length=255, default="")
  show_name = models.BooleanField(default=True)
  participates = models.BooleanField(default=False)
  has_payed = models.BooleanField(default=False)
  
  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['email', 'event'], name='unique_event_email_combination'
      )
    ]