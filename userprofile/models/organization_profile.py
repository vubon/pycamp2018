from django.db import models
from django.contrib.postgres.fields import JSONField

from userprofile.models.user_profile_basic import UserProfileBasic


class OrganizationProfile(UserProfileBasic):
    organization_name = models.CharField(max_length=100)
    is_training_institute = models.BooleanField(default=False)
    industry_type = JSONField(null=True, blank=True)
    website = models.URLField(max_length=100)
    founded_on = models.DateField()
    company_size = JSONField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    additional_contact = models.TextField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.organization_name
