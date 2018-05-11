import uuid
from django.contrib.auth.models import User
from django.db import models


class UserProfileBasic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=11)
    current_address = models.TextField(max_length=500)
    status = models.BooleanField(default=True)
    gravatar = models.CharField(max_length=100)
    guid = models.UUIDField(default=uuid.uuid4, editable=False)

    # class Meta:
    #     abstract = True
