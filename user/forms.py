from django import forms
from .models import UserProfileBasic, PersonalProfile, OrganizationProfile

class ProfileBasic(forms.ModelForm):
    class meta:
        model = UserProfileBasic
        fields = '__all__'
        label = [


        ]
