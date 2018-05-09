from django.db import models
from django.contrib.postgres.fields import JSONField

from userprofile.models import UserProfileBasic
from events.models.event_basic import EventBasic
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


class EventTrainer(EventBasic):
    trainer = models.ForeignKey(
        UserProfileBasic,
        on_delete=models.CASCADE,
        related_name='event_trainer',
        related_query_name='trainer'
    )
    rating = JSONField(default={})
    status = models.BooleanField(default=True)

    object = EventTrainerManager()
