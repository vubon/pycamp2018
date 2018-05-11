from django.db import models
from django.contrib.postgres.fields import JSONField

from events.models.event_basic import EventBasic


class EventDetail(EventBasic):
    # event_user = models.OneToOneField(EventBasic, on_delete=models.CASCADE, primary_key=True)
    open_for_all = models.BooleanField(default=False)
    screening_process = models.URLField(max_length=100, blank=True)
    registration_process = models.TextField(default='', blank=True)
    payment_process = models.URLField(max_length=150, blank=True)
    additional_fees = models.FloatField(null=True, blank=True)
    review_event_host = JSONField(default={}, blank=True)