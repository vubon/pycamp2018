from django.urls import path


from . import views


urlpatterns = [
    path('create_profile/', views.create_profile, name='create_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('create_org_profile/', views.create_organization_profile, name='create_organization_profile'),
    path('update_org_profile/', views.update_organization_profile, name='update_organization_profile'),
    path('profile_details/<int:pk>/', views.ProfileDetails.as_view(), name='profile_details')
]