from django.db import models
from django.contrib.auth.models import User

from userprofile.models.personal_profile import PersonalProfile
from jobpost.models.job_post_basic import JobPostBasic
from jobpost.models.job_applicant_queryset import JobApplicantQuerySet


class JobApplicantManager(models.Manager):
    """
        Find Job applicants
    """

    def get_queryset(self):
        return JobApplicantQuerySet(self.model, using=self._db)

    def all_applicant(self,id):
        return self.get_queryset().all_applicant(id)

    def selected_applicant(self):
        return self.get_queryset().selected_applicant()

    def get_job_applicant(self,j_id,a_id):
        return self.get_queryset().get_job_applicant(j_id,a_id)


class JobApplicant(models.Model):
    job = models.ForeignKey(JobPostBasic,on_delete=models.CASCADE)
    applicant = models.ForeignKey(User,on_delete=models.CASCADE)
    selection_confirmation= models.BooleanField(default=False)
    call_for_interview = models.BooleanField(default=False)
    apply_status = models.BooleanField(default=False)

    objects = JobApplicantManager()
