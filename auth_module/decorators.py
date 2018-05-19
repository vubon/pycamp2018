from django.shortcuts import redirect
from django.urls import reverse

from userprofile.models import UserProfileBasic


def profile_required():
    def wrapper(func):
        def _view(request, *args, **kwargs):
            try:
                user_profile_basic = UserProfileBasic.objects.get(auth=request.user)
                return func(request, *args, **kwargs)
            except UserProfileBasic.DoesNotExist:
                return redirect('userprofile:create_profile', username=request.user.username)
        return _view
    return wrapper