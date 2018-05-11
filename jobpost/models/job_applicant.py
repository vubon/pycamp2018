from django.db import models

from userprofile.models.personal_profile import PersonalProfile
from jobpost.models.job_post_basic import JobPostBasic
from jobpost.models.job_applicant_queryset import JobApplicantQuerySet


class JobApplicantManager(models.Model):
    """
        Find Job applicants
    """

    def get_queryset(self):
        return JobApplicantQuerySet(self.model, using=self._db)

    def all_applicant(self):
        return self.get_queryset().all_applicant()

    def selected_applicant(self):
        return self.get_queryset().selected_applicant()


class JobApplicant(models.Model):
    job_id = models.ForeignKey(JobPostBasic, on_delete=models.CASCADE)
    applicant_id = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE)
    selection_confirmation= models.BooleanField(default=False)
    call_for_interview = models.BooleanField(default=False)

    object = JobApplicantManager()
