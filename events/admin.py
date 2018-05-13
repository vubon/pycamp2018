from django.contrib import admin

from . models import  EventTrainer, EventParticipant

# Register your models here.
admin.site.register(EventTrainer)
admin.site.register(EventParticipant)