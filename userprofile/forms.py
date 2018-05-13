from django import forms
from django.contrib.auth.models import User

from .models import PersonalProfile, OrganizationProfile


class BaseUserForm(forms.ModelForm):
    field_order = ['first_name', 'last_name']

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class IndividualProfileForm(forms.ModelForm):

    field_order = ['first_name', 'last_name']

    class Meta:
        model = PersonalProfile
        exclude = ['auth', 'username', 'email', 'password', 'is_trainer',
                   'status', 'gravatar']


class OrganizationModelForm(forms.ModelForm):
    # website = forms.URLField(max_length=100, widget=forms.Textarea)
    field_order = ['organization_name', 'contact', 'industry_type',
                   'description', 'additional_contact', 'website',
                   'company_size', 'founded_on', 'is_training_institute']

    class Meta:
        model = OrganizationProfile
        exclude = ['auth', 'username',
                   'email', 'password', 'is_approved', 'status']

