from django.db import models
from django.contrib.postgres.fields import JSONField

from events.models.event_basic import EventBasic


class EventDetail(EventBasic):
    open_for_all = models.BooleanField(default=False)
    screening_process = models.URLField(max_length=100)
    registration_process = models.TextField(default='')
    payment_process = models.URLField(max_length=150)
    additional_fees = models.FloatField(null=True)
    review_event_host = JSONField(default={})