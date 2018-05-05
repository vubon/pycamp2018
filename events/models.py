import uuid
from django.db import models

# from jsonfield import JSONField

from django.contrib.postgres.fields import JSONField
from django.core.files.storage import FileSystemStorage

# Create your models here.

fs = FileSystemStorage(location='')


class EventBasic(models.Model):
    uiqueid_event = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, default='')
    start_date = models.DateField(auto_now_add=False, null=True)
    end_date = models.DateField(null=True, blank=True)
    registration_deadline = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    banner = models.ImageField(storage=fs, null=True)
    audienceT_type = JSONField(default={})
    max_audience = models.IntegerField(default=0)
    venue = JSONField(default={})
    venue_coordinate = JSONField(default={})
    region = JSONField(default={})
    cuurency = JSONField(default={})
    registration_fee = models.FloatField(null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class EventDetail(EventBasic):
    open_for_all = models.BooleanField(default=False)
    screening_process = models.URLField(max_length=100)
    registration_process = models.TextField(default='')
    payment_process = models.URLField(max_length=150)
    additional_fees = models.FloatField(null=True)
    review_event_host = JSONField(default={})


class EventTrainer(EventBasic):
    # trainerID = models.ForeignKey( {TRAINER_BUILD}, models.CASCADE)
    rating = JSONField(default={})
    status = models.BooleanField(default=False)


class EventParticipant(EventBasic):
    # participantID = models.ForeignKey()
    status_participant = models.BooleanField(default=True)
    is_selection_pass = models.BooleanField(default=False)
    payment_confirmed = models.BooleanField(default=False)
    registrationC_complete = models.BooleanField(default=False)
    review_participant = JSONField(default={})
    rating_participant = JSONField(default={})
    confirmation_text = JSONField(default={})
