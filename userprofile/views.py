from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import FormView
from django.contrib.auth.models import User

from .forms import IndividualProfileForm, BaseUserForm
from .models import UserProfileBasic, PersonalProfile, OrganizationProfile


def create_profile(request):
    if request.method == 'POST':
        print(request.POST)
        user_form = BaseUserForm(request.POST, instance=request.user)
        profile_form = IndividualProfileForm(request.POST)

        if all([user_form.is_valid(), profile_form.is_valid()]):
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.auth = user
            profile.save()
            return redirect('home')

    user_form = BaseUserForm(instance=request.user)
    profile_form = IndividualProfileForm()
    return render(request, 'userprofile/create_profile.html',
                  {'user_form': user_form, 'profile_form': profile_form})

#
# class CreateProfile(FormView):
#     form_class = IndividualProfileForm
#     template_name = 'userprofile/create_profile.html'
#
#     def get(self, request, *args, **kwargs):
#         user = get_object_or_404(User, username=request.user)
#         initial_data = {
#             'first_name': user.first_name,
#             'last_name': user.last_name,
#
#         }
#         form = self.form_class(initial=initial_data)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         # print(request.POST)
#         user = get_object_or_404(User, username=request.user)
#         initial_data = {
#             'first_name': user.first_name,
#             'last_name': user.last_name
#         }
#         form = IndividualProfileForm(data=request.POST, initial=)
#         # first_name = form.cleaned_data['first_name']
#         print(form.__dict__)
#         return render(request, self.template_name, {'form': form})

