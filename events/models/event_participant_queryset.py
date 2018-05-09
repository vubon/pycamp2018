from django.db import models


class EventParticipantQuerySet(models.QuerySet):
    """
        Details about event participants
    """

    def all_participant(self):
        return self.filter(registration_complete=True, participant_status=True)


    def selected_participant(self):
        return self.filter(is_selection_pass=True, participant_status=True)


    def paid_participant(self):
        return self.filter(payment_confirmed=True, participant_status=True)
