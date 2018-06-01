from django.db import models


class JobApplicantQuerySet(models.QuerySet):
    """
        Details about job applicants
    """

    def all_applicant(self):
        return self.all()

    def selected_applicant(self):
        return self.filter(selection_confirmation=True)

    def get_job_applicant(self,j_id,a_id):
        return self.get(applicant_id=a_id,job_id=j_id)

    def get_applicant_list(self,job_id):
        return self.defer('applicant').filter(job_id=job_id)

    def get_applied_job(self,user_id):
        return self.defer('job').filter(applicant_id = user_id)
