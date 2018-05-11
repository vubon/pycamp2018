from django.db import models
from django.contrib.postgres.fields import JSONField

from events.models.event_basic import EventBasic


class EventDetail(EventBasic):
    # event_user = models.OneToOneField(EventBasic, on_delete=models.CASCADE, primary_key=True)
    open_for_all = models.BooleanField(default=False)
    screening_process = models.URLField(max_length=100, blank=True, null=True)
    registration_process = models.TextField(null=True, blank=True)
    payment_process = models.CharField(max_length=250, blank=True, null=True)
    additional_fees = models.FloatField(null=True, blank=True)
    review_event_host = JSONField(blank=True, null=True)