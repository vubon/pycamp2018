from django import forms

from .models.job_post_basic import JobPostBasic
from .models.job_post_detail import JobPostDetails


class JobPostBasicForm(forms.ModelForm):
    class Meta:
        model=JobPostBasic
        #fields = '__all__'
        fields = ["job_title", "salary_range", "is_part_time", "position", "stack", "vacancy", "deadline"]

class JobPostDetailsForm(forms.ModelForm):
    class Meta:
        model=JobPostDetails
        #fields = '__all__'
        fields = ["description", "application_process", "screening_details"]

