from django.db import models


class EventTrainerQuerySet(models.QuerySet):
    """
        Details About Trainer
    """

    def event_trainer(self):
        return self.filter(status=True)
