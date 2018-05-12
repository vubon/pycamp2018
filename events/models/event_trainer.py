from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField

from userprofile.models import PersonalProfile
from events.models.event_basic import EventBasic


class EventTrainer(EventBasic):
    trainer = models.ForeignKey(
        PersonalProfile,
        on_delete=models.CASCADE,
        related_name='event_trainer',
        related_query_name='trainer'
    )
    rating = JSONField(default={})
    status = models.BooleanField(default=False)
