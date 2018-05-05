from django.db import models

import uuid
from datetime import datetime, date

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField


##### Managers Start ######
class UserQueryset(models.QuerySet):
    def regular_user(self):
        return self.filter(is_trainer=False)

    def trainer(self):
        return self.filter(is_trainer=True)


class UserManager(models.Manager):
    def get_queryset(self):
        return UserQueryset(self.model, using=self._db)

    def regular_user(self):
        return self.get_queryset().regular_user()

    def trainer(self):
        return self.get_queryset().trainer()

    def experience_of(self, months):
        return self.get_queryset().trainer().filter(experience=months)


##### Managers End ######


class UserProfileBasic(models.Model):
    auth = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    address = models.TextField()
    status = models.CharField(max_length=45, blank=True, null=True)
    gravatar = models.CharField(max_length=200, blank=True, null=True)
    guid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class PersonalProfile(UserProfileBasic):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )

    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER)
    is_trainer = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    education = JSONField(blank=True, null=True)
    experience = JSONField(blank=True, null=True)
    experience_years = models.IntegerField(help_text='experience in months', default=0)
    current_organization = models.TextField(blank=True, null=True)
    official_contact = models.CharField(max_length=13)
    # objects = models.Manager()
    user = UserManager()

    @property
    def age(self):
        return (date.today() - self.date_of_birth).days

    def __str__(self):
        return self.auth.first_name + ' ' + self.auth.last_name


class OrganizationProfile(UserProfileBasic):
    title = models.CharField(max_length=100)
    is_training_institute = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    industry_type = models.CharField(max_length=50)
    website = models.URLField(max_length=100, blank=True, null=True)
    founded_on = models.DateField()
    company_size = models.CharField(max_length=100)
    additional_contact = models.CharField(max_length=13, blank=True, null=True)
    is_approved = models.BooleanField(default=False)


class EventCreateView(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
