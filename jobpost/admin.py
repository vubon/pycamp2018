from django.contrib import admin

from .models import JobApplicant, JobPostBasic, JobPostDetails
# Register your models here.

admin.site.register(JobPostBasic)
admin.site.register(JobPostDetails)
admin.site.register(JobApplicant)