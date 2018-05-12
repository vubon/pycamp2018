# import uuid
from django.db import models

from django.contrib.postgres.fields import JSONField
from django.core.files.storage import FileSystemStorage

from events.models.event_basic_queryset import EventQuerySet

# Create your models here.
fs = FileSystemStorage(location='')


class EventBasicManager(models.Manager):
    """
        comment here purpose of whole manager or activity
    """
    def get_queryset(self):
        """
        :return:
        """
        return EventQuerySet(self.model, using=self._db)

    def event_basic_details(self):
        """

        :return:
        """
        return self.get_queryset().event_queryset()

    def create_event(self, request_data):
        """

        :param request_data:
        :return:
        """
        pass


class EventBasic(models.Model):
    # unique_event = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, null=True, blank=False)
    start_date = models.DateField(auto_now_add=False, null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    registration_deadline = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    banner = models.ImageField(storage=fs, null=True, blank=True)
    audience_type = JSONField(null=True, blank=True)
    max_audience = models.IntegerField(default=0, null=True, blank=True)
    venue = JSONField(default={}, blank=True, null=True)
    venue_coordinate = JSONField(null=True, blank=True)
    region = JSONField(null=True, blank=True)
    currency = JSONField(null=True, blank=True)
    registration_fee = models.FloatField(null=True, blank=True)

    objects = EventBasicManager()

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

