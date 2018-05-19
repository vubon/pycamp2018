from django.urls import path


from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('create_org_profile/', views.create_organization_profile, name='create_organization_profile'),
    path('update_org_profile/', views.update_organization_profile, name='update_organization_profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('delete_user/', views.del_user, name='del_user'),
    path('profile_details/<int:pk>/', views.ProfileDetails.as_view(), name='profile_details')
]
