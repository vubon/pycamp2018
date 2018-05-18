from django.db import models
from django.contrib.postgres.fields import JSONField

from userprofile.models import UserProfileBasic
from events.models.event_basic import EventBasic
from events.models.event_participant_queryset import EventParticipantQuerySet


class EventParticipantManager(models.Manager):
    """
        To find all participant list of the event;
        To find selected participant list of the event;
        To find paid participant list of the event;
    """
    def get_queryset(self):
        """
            :return event participant queryset object
        """
        return EventParticipantQuerySet(self.model, using=self._db)

    def all_participant(self):
        """
            return all registerd participant list of the event
        """
        return get_queryset().all_participant()

    def selected_participant(self):
        """
            return selected participant list of the event
        """
        return get_queryset().selected_participant()

    def paid_participant(self):
        """
            return paid participant list of the event
        """
        return get_queryset().paid_participant()


class EventParticipant(EventBasic):
    participant = models.ForeignKey(
        UserProfileBasic,
        on_delete=models.CASCADE,
        related_name='event_participant',
        related_query_name='participant'
    )

    registration_complete = models.BooleanField(default=False)
    is_selection_pass = models.BooleanField(default=False)
    payment_confirmed = models.BooleanField(default=False)
    review_participant = JSONField(default={})
    rating_participant = JSONField(default={})
    confirmation_text = JSONField(default={})
    participant_status = models.BooleanField(default=True)

    objects = EventParticipantManager()
