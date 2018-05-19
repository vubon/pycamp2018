from django.contrib import admin

# Register your models here.
from .models import PersonalProfile, OrganizationProfile

# Register your models here.

admin.site.register(PersonalProfile)
admin.site.register(OrganizationProfile)