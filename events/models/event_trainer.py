from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField

from userprofile.models import PersonalProfile
from events.models.event_details import EventDetail
from events.models.event_trainer_queryset import EventTrainerQuerySet


class EventTrainerManager(models.Manager):
    """
        get event trainer details
    """

    def get_queryset(self):
        """
            return queryset
        """
        return EventTrainerQuerySet(self.model, using=self._db)

    def event_trainer(self):
        """
            return trainer list
        """
        return self.get_queryset().event_trainer()


class EventTrainer(models.Model):
    event_title = models.ForeignKey(EventDetail, on_delete=models.CASCADE, null=True)
    trainer = models.ForeignKey(
        PersonalProfile,
        on_delete=models.CASCADE,
        related_name='event_trainer',
        related_query_name='trainer'
    )
    rating = models.FloatField(default=0, max_length=10)
    status = models.BooleanField(default=True)

    # object = EventTrainerManager()
