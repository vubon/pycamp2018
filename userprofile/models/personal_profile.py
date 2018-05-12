from django.db import models
from django.contrib.postgres.fields import JSONField

from userprofile.models.user_profile_basic import UserProfileBasic
from userprofile.models.personal_profile_queryset import PersonalProfileQuerySet


class PersonalProfileManager(models.Manager):
    """
        Find Trainee or Regular  User
        Find Trainer
    """

    def get_queryset(self):
        return PersonalProfileQuerySet(self.model, using = self._db)

    def regular_user(self):
        """
            return regular user / Trainee
        """

        return self.get_queryset().regular_user()

    def trainer(self):
        """
            return trainer
        """

        return self.get_queryset().trainer()
        

class PersonalProfile(UserProfileBasic):
    GENDER_STATUS = (
        ('m', 'Male'),
        ('f', 'Female'),
    )

    EXPERIENCE = (
        ('entry', 'Entry Level'),
        ('1-2', '1-2 years'),
        ('3-5', '3-5 years'),
        ('6-10', '6-10 years'),
        ('above 10', 'Above 10 years')
    )

    about = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_STATUS, null=True, blank=True)
    is_trainer = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    education = JSONField(null=True, blank=True)
    experience = models.CharField(max_length=20, choices=EXPERIENCE, null=True, blank=True)
    permanent_address = models.TextField(max_length=1000)
    interest = JSONField(null=True, blank=True)
    current_organization = models.TextField(max_length=100)
    official_contact = models.TextField()
    reference = models.TextField()

    object = PersonalProfileManager()

    def __str__(self):
        if self.auth:
            return self.auth.first_name + ' ' + self.auth.last_name
        return "auth does not exist"
