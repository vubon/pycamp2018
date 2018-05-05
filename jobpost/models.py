from django.db import models
from userprofile.mdoels import  OrganizationProfile
# Create your models here.
class JobPostBasic(models.Model):
    organization_id = models.ForeignKey(OrganizationProfile,on_delete=models.CASCADE)
    job_title = models.CharField(max_length=256)
    salary_range = models.CharField(max_length=256)
    is_partime = models.BooleanField(default=False)
    position = models.CharField(max_length=256)
    stack = models.TextField()
    vacancy = models.PositiveIntegerField()
    deadline = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.job_title


class JobPostDetails(JobPostBasic):
    description = models.TextField()
    application_process = models.TextField()
    sreening_details = models.TextField()
