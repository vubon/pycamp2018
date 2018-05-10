from django.contrib import admin

from . models import EventDetail, EventTrainer, EventParticipant

# Register your models here.
admin.site.register(EventDetail)
admin.site.register(EventTrainer)
admin.site.register(EventParticipant)