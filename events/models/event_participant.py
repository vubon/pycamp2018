from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField

from userprofile.models import PersonalProfile
from events.models.event_details import EventDetail
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
        return self.get_queryset().all_participant()

    def selected_participant(self):
        """
            return selected participant list of the event
        """
        return self.get_queryset().selected_participant()

    def paid_participant(self):
        """
            return paid participant list of the event
        """
        return self.get_queryset().paid_participant()


class EventParticipant(models.Model):
    event_title = models.ForeignKey(EventDetail, on_delete=models.CASCADE, null=True)
    participant_id = models.ForeignKey(
        PersonalProfile,
        on_delete=models.CASCADE,
        related_name='event_participant',
        related_query_name='participant'
    )

    registration_complete = models.BooleanField(default=False)
    is_selection_pass = models.BooleanField(default=False)
    payment_confirmed = models.BooleanField(default=False)
    review_participant = JSONField(default={}, null=True, blank=True)
    rating_participant = JSONField(default={}, null=True, blank=True)
    confirmation_text = JSONField(default={}, null=True, blank=True)
    participant_status = models.BooleanField(default=True)

    # participant = EventParticipantManager()
