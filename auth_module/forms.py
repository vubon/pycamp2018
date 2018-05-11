from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class IndividualSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=80)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )


class OrganizationSignUpForm(UserCreationForm):
    # organization_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=80)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class SignInForm(AuthenticationForm):

    def confirm_login_allowed(self, user):
        # if not user.is_active or not user.is_validated:
        #     raise forms.ValidationError('There was a problem with your login.', code='invalid_login')
        pass