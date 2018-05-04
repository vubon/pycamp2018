from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Event(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    total_student = models.PositiveIntegerField(default=0)
    total_trainer = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.event_name
