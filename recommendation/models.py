from django.db import models

from userprofile.models import UserProfileBasic
from events.models import EventBasic


# Create your models here.

class PersonalRecommendation(models.Model):
    profile_id = models.ForeignKey(
        UserProfileBasic,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    trainer_id = models.ForeignKey(
        UserProfileBasic,
        on_delete=models.CASCADE,
        related_name='rec_trainer'
    )
    event_id = models.ForeignKey(
        EventBasic,
        on_delete=models.CASCADE,
        related_name='rec_event'
    )
    remarks = models.TextField()
    status = models.BooleanField(default=True)
