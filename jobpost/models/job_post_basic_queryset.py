from django.db import models


class JobPostQuerySet(models.QuerySet):
    """
        Detail about job post query set
    """

    def job_title(self):
        """
            Get all job post
        """

        return self.defer('job_title','vacancy', 'deadline','id').filter(status=True)

    def my_job(self,id):
        # return self.defer('job_title','id','organization_id').filter(organization_id=id,status=True)
        return self.defer('job_title','vacancy', 'deadline','id').filter(organization_id=id,status=True)
