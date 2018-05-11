from django.db import models


class OrganizationProfileQuerySet(models.QuerySet):
    """
        Details about Organization
    """
    def training_organization(self):
        """
            return training institute
        """
        return self.filter(is_training_institute=True)

    def employer_organization(self):
        """
            return employer organization
        """
        return self.filter(is_training_institute=False)
