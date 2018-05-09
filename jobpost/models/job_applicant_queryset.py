from django.db import models


class JobApplicantQuerySet(models.QuerySet):
    """
        Detials about job applicants
    """

    def all_applicant(self):
        return self.all()

    def selected_applicant(self):
        return self.filter(selection_confirmation=True)
