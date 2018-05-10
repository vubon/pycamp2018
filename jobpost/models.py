from django.db import models
from userprofile.models import  OrganizationProfile,PersonalProfile
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



    def __str__(self):
        return self.job_title


class JobPostDetails(models.Model):
    job_id = models.ForeignKey(JobPostBasic,on_delete=models.CASCADE)
    description = models.TextField()
    application_process = models.TextField()
    sreening_details = models.TextField()


class JobApplicant(models.Model):
    job_id = job_id = models.ForeignKey(JobPostBasic,on_delete=models.CASCADE)
    applicant_id = models.ForeignKey(PersonalProfile,on_delete=models.CASCADE)
    selection_confiramtion= models.BooleanField(default=False)
    call_for_interview = models.BooleanField(default=False)
