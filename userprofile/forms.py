from django import forms
from django.contrib.auth.models import User

from .models import PersonalProfile


class BaseUserForm(forms.ModelForm):
    field_order = ['first_name', 'last_name']

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class IndividualProfileForm(forms.ModelForm):
    # first_name = forms.CharField(label='First Name', max_length=100)
    # last_name = forms.CharField(label='Last Name', max_length=100)
    # contact = forms.EmailField(label='Email', max_length=100)
    # current_address = forms.CharField(widget=forms.Textarea)
    # about = forms.CharField(widget=forms.Textarea)
    # date_of_birth = forms.DateField()
    # gender = forms.CharField()

    field_order = ['first_name', 'last_name']

    class Meta:
        model = PersonalProfile
        exclude = ['auth', 'username', 'email', 'password', 'is_trainer',
                   'status', 'gravatar']

