from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.signals import pre_save
from django.urls import reverse

from events.models.event_basic import EventBasic
from events.utils import unique_slug_generator


class EventDetail(EventBasic):
    open_for_all = models.BooleanField(default=False)
    screening_process = models.URLField(max_length=100, null=True, blank=True)
    registration_process = models.TextField(default='')
    payment_process = models.URLField(max_length=150, null=True, blank=True)
    additional_fees = models.FloatField(null=True)
    review_event_host = JSONField(default={})

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


def ed_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(ed_pre_save_receiver, sender=EventDetail)