from django.db import models
from django.contrib.postgres.fields import JSONField

from userprofile.models import PersonalProfile
from events.models.event_basic import EventBasic

class EventParticipant(EventBasic):
    participant_id = models.ForeignKey(
        PersonalProfile,
        on_delete=models.CASCADE,
        related_name='event_participant',
        related_query_name='participant'
    )
    status_participant = models.BooleanField(default=True)
    is_selection_pass = models.BooleanField(default=False)
    payment_confirmed = models.BooleanField(default=False)
    registrationC_complete = models.BooleanField(default=False)
    review_participant = JSONField(default={})
    rating_participant = JSONField(default={})
    confirmation_text = JSONField(default={})
