from django import forms

from userprofile.models.user_profile_basic import UserProfileBasic


class UserProfileBasicForm(forms.ModelForm):
    class Meta:
        model = UserProfileBasic
        fields = ['contact', 'current_address', 'status', 'gravatar']

class
