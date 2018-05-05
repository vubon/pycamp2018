from django.contrib import admin

# Register your models here.
from .models import UserProfileBasic, PersonalProfile, OrganizationProfile

# Register your models here.


admin.site.register(UserProfileBasic)
admin.site.register(PersonalProfile)
admin.site.register(OrganizationProfile)