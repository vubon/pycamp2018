from django.db import models
from django.contrib.postgres.fields import JSONField

from userprofile.models.user_profile_basic import UserProfileBasic
from userprofile.models.organization_profile_queryset import OrganizationProfileQuerySet


class OrganizationProfileManager(models.Manager):
    """
        Find Training Organization
        Find Employer Organization
    """

    def get_queryset(self):
        """
            return query set
        """

        return OrganizationProfileQuerySet(self.model, using = self._db)

    def training_organization(self):
        """
            return training organization
        """

        return self.get_queryset().training_organization()

    def employer_organization(self):
        """
        return employer organization
        """

        return self.get_queryset().employer_organization()


class OrganizationProfile(UserProfileBasic):
    organization_name = models.CharField(max_length=100)
    is_training_institute = models.BooleanField(default=True)
    industry_type = JSONField(null=True, blank=True)
    website = models.URLField(max_length=100)
    founded_on = models.DateField()
    company_size = JSONField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    additional_contact = models.TextField()
    is_approved = models.BooleanField(default=False)

    object = OrganizationProfileManager()

    def __str__(self):
        return self.organization_name
