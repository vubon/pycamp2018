import uuid
from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField


class UserProfileBasic(models.Model):
    auth = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=11)
    current_address = models.TextField(max_length=500)
    status = models.BooleanField(default=True)
    gravatar = models.CharField(max_length=100)
    guid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class PersonalProfile(UserProfileBasic):
    GENDER_STATUS = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    EXPERIENCE = (
        ('entry', 'Entry Level'),
        ('1-2', '1-2 years'),
        ('3-5', '3-5 years'),
        ('6-10', '6-10 years'),
        ('above 10', 'Above 10 years')
    )

    about = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_STATUS, null=True, blank=True)
    is_trainer = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    education = JSONField(null=True, blank=True)
    experience = models.CharField(max_length=20, choices=EXPERIENCE, null=True, blank=True)
    permanent_address = models.TextField(max_length=1000)
    interest = JSONField(null=True, blank=True)
    current_organization = models.TextField(max_length=100)
    official_contact = models.TextField()
    reference = models.TextField()

    def __str__(self):
        return self.auth.first_name + ' ' + self.auth.last_name


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


