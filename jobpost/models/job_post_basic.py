from django.db import models
import uuid

from django.urls import reverse
from jobpost.models.job_post_basic_queryset import JobPostQuerySet
from userprofile.models.organization_profile import OrganizationProfile
from django.contrib.auth.models import User

class JobPostBasicManager(models.Manager):
    """
        Find Job query with job title
    """

    def get_queryset(self):
        return JobPostQuerySet(self.model, using=self._db)

    def job_title(self):
        """
            Return Job title
        """

        return self.get_queryset().job_title()


class JobPostBasic(models.Model):
    organization_id = models.ForeignKey(User,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=256)
    salary_range = models.CharField(max_length=256)
    is_part_time = models.BooleanField(default=False)
    position = models.CharField(max_length=256)
    stack = models.TextField()
    vacancy = models.PositiveIntegerField()
    deadline = models.DateField()
    guid = models.UUIDField(default=uuid.uuid4, editable=False)

    def create_job_post(self,request_data):

        pass

    object = JobPostBasicManager()

    def __str__(self):
        return self.job_title

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('job_post_detail', args=[str(self.id)])
