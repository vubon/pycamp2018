from django.db import models

from jobpost.models.job_post_basic import JobPostBasic


class JobPostDetails(models.Model):
    jobpostbasic = models.OneToOneField(JobPostBasic, on_delete=models.CASCADE)
    description = models.TextField()
    application_process = models.TextField()
    screening_details = models.TextField()
