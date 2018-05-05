from django.db import models
from django.contrib.postgres.fields import JSONField


class UserProfileBasic(models.Model):
	auth = models.OneToOneField(User, on_delete=models.CASCADE)
	contact = models.CharField(max_length=11)
	current_address = models.TextField(max_length=500)
	date_joined = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)
	gravatar = models.CharField(max_length=100)
	guid = models.CharField(max_length=40)

	class Meta:
		abstract = True

	def __str__(self):
		return self.name

Experience = (
	('entry', 'Entry Level'),
	('1-2', '1-2 years'),
	('3-5', '3-5 years'),
	('6-10', '6-10 years'),
	('above 10', 'Above 10 years')
)

Gender_status = (
	('male', 'Male'),
	('female', 'Female'),

)

class PersonalProfile(UserProfileBasic):
	about = models.TextField(blank=True, null=True)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=10, choices=Gender_status, null=True, blank=True)
	is_trainer = models.BooleanField(default=False)
	is_student = models.BooleanField(default=False)
	education = JSONField()
	experience = models.CharField(max_length=20, choices=Experience, null=True, blank=True)
	permanent_address = models.TextField(max_length=1000)
	interest = JSONField()
	current_organization = models.TextField(max_length=100)
	official_contact = models.TextField()
	reference = models.TextField()

	def __str__(self):
		return self.name

class OrganizationProfile(UserProfileBasic):
	organization_name = models.CharField(max_length=100)
	is_training_instute = models.BooleanField(default=False)
	industry_type = JSONField() # I didn't write Taxonomy Model yet. So, just for now I write jsonfield. Later will add taxonomy Model
	website = models.URLField(max_length=20)
	founded_on = models.DateField()
	company_size = JSONField()
	description = models.TextField(null=True, blank=True)
	addtional_contact = models.TextField()
	is_approved = models.BooleanField(default=False)

	def __str__(self):
		return self.name


