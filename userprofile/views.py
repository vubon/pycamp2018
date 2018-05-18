from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import ObjectDoesNotExist
# from django.views.generic import FormView
# from django.contrib.auth.models import User

from .forms import IndividualProfileForm, BaseUserForm, OrganizationModelForm
from .models import PersonalProfile, OrganizationProfile, UserProfileBasic


def individual_profile_creation_check(user):
    return not user.user_profile.is_organization


def dashboard(request, username):
    user = UserProfileBasic.objects.get(auth=request.user)
    return render(request, 'base/base.html', {'userbasic': user})


@login_required(login_url='/signin/')
# @user_passes_test(individual_profile_creation_check)
def create_profile(request, username):
    if request.method == 'POST':
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


@login_required(login_url='/signin/')
def update_profile(request, username):
    user = request.user
    if request.method == 'POST':
        user_form = BaseUserForm(request.POST, instance=user)
        personal_profile = PersonalProfile.objects.filter(auth=request.user)[0]
        profile_form = IndividualProfileForm(request.POST, instance=personal_profile)

        if all([user_form.is_valid(), profile_form.is_valid()]):
            user = user_form.save()
            profile = profile_form.save()
            profile.auth = user
            profile.save()
            return redirect('home')

    user_form = BaseUserForm(instance=request.user)
    personal_profile = PersonalProfile.objects.filter(auth=request.user)
    profile_form = IndividualProfileForm(instance=personal_profile[0])

    return render(request, 'userprofile/create_profile.html',
                  {'user_form': user_form, 'profile_form': profile_form})


@login_required(login_url='/signin/')
def create_organization_profile(request, username):
    if request.method == 'POST':
        organization_profile_form = OrganizationModelForm(request.POST)
        print(request.POST)
        if organization_profile_form.is_valid():
            # user = user_form.save()
            profile = organization_profile_form.save(commit=False)
            profile.auth = request.user
            profile.save()
            return redirect('home')

    # user_form = BaseUserForm(instance=request.user)
    organization_profile_form = OrganizationModelForm()
    return render(request, 'userprofile/create_org_profile.html',
                  {'profile_form': organization_profile_form})


@login_required(login_url='/signin/')
def update_organization_profile(request, username):
    if request.method == 'POST':
        # user_form = BaseUserForm(request.POST, instance=request.user)
        organization_profile = OrganizationProfile.objects.get(auth=request.user)
        organization_profile_form = OrganizationModelForm(request.POST, instance=organization_profile)

        if organization_profile_form.is_valid():
            # user = user_form.save()
            profile = organization_profile_form.save(commit=False)
            profile.auth = request.user
            profile.save()
            return redirect('home')

    organization_profile = OrganizationProfile.objects.get(auth=request.user)
    organization_profile_form = OrganizationModelForm(instance=organization_profile)

    return render(request, 'userprofile/create_org_profile.html',
                  {'profile_form': organization_profile_form})


def delete_profile(request, username):
    user = request.user
    user.is_active = False
    user.save()
    return render(request, 'userprofile/deactivation_profile.html')


# @staff_member_required
def del_user(request, username):
    user = request.user
    try:
        # u = User.objects.get(username = username)
        user.delete()
        # messages.sucess(request, "The user is deleted")
        return redirect('home')


    except User.DoesNotExist:
        # messages.error(request, "User doesnot exist")
        return redirect('home')
    #
    # except Exception as e:
    #     return render(request, 'front.html',{'err':e.message})
    #
    # return render(request, 'front.html')


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

