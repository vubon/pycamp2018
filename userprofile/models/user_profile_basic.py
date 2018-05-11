import uuid
from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField


class UserProfileBasic(models.Model):
    auth = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, related_name='user_profile')
    contact = models.CharField(max_length=11)
    current_address = models.TextField(max_length=500)
    status = models.BooleanField(default=True)
    gravatar = models.CharField(max_length=100)
    guid = models.UUIDField(default=uuid.uuid4, editable=False)

    # class Meta:
    #     abstract = True