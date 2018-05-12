from django.db import models


class PersonalProfileQuerySet(models.QuerySet):
    """
        Details about Personal Profile
    """

    def regular_user(self):
        """
            Return Trainee or Regular User
        """

        return self.filter(is_trainer=False)

    def trainer(self):
        """
            Return Trainer
        """

        return self.filter(is_trainer=True)
