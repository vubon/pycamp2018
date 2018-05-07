from django.db import models


class EventQuerySet(models.QuerySet):
    """
     details about Event Query set
    """

    def event_queryset(self):
        return self.filter(title='event title')
