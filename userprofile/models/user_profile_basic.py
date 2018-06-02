import uuid
from django.contrib.auth.models import User
from django.db import models

from userprofile.models.user_profile_basic_queryset import UserProfileBasicQuerySet


class UserProfileBasicManager(models.Manager):
    
    def get_queryset(self):
        return UserProfileBasicQuerySet(self.model, using=self._db)

    def get_organization_status(self,user_id):
        return self.get_queryset().get_organization_status(user_id)


class UserProfileBasic(models.Model):
    auth = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, related_name='user_profile')
    contact = models.CharField(max_length=11)
    current_address = models.TextField(max_length=500)
    status = models.BooleanField(default=True)
    gravatar = models.CharField(max_length=100)
    guid = models.UUIDField(default=uuid.uuid4, editable=False)
    is_organization = models.BooleanField(default=False)

    objects = UserProfileBasicManager()

    # class Meta:
    #     abstract = True

    def __str__(self):
        if self.auth:
            return self.auth.username
        return "auth does not exist"
