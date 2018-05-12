from django.contrib.auth.models import User
from django.db import models

from userprofile.models import PersonalProfile
from events.models import EventDetail


# Create your models here.

class PersonalRecommendation(models.Model):
    profile_id = models.ForeignKey(
        PersonalProfile,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    trainer_id = models.ForeignKey(
        PersonalProfile,
        on_delete=models.CASCADE,
        related_name='rec_trainer'
    )
    event_id = models.ForeignKey(
        EventDetail,
        on_delete=models.CASCADE,
        related_name='rec_event'
    )
    remarks = models.TextField()
    status = models.BooleanField(default=True)
