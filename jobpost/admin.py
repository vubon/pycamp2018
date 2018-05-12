from django.contrib import admin

from .models.job_applicant import  JobApplicant
from .models.job_post_basic import JobPostBasic
from .models.job_post_detail import JobPostDetails
# Register your models here.

admin.site.register(JobPostBasic)
admin.site.register(JobPostDetails)
admin.site.register(JobApplicant)
