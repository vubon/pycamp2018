# import uuid
from django.db import models

from django.contrib.postgres.fields import JSONField
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import settings

from events.models.event_basic_queryset import EventQuerySet


# Create your models here.
fs = FileSystemStorage(location='media/event_img/')
User = settings.AUTH_USER_MODEL


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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, default='', null=True)
    start_date = models.DateField(auto_now_add=False, null=True)
    end_date = models.DateField(null=True, blank=True)
    registration_deadline = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    banner = models.ImageField(storage=fs, null=True)
    audience_type = JSONField(default={})
    max_audience = models.IntegerField(default=0)
    venue = models.CharField(max_length=150)
    venue_coordinate = models.CharField(max_length=100)
    region = JSONField(default={})
    currency = JSONField(default={})
    registration_fee = models.FloatField(null=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    objects = EventBasicManager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.title
