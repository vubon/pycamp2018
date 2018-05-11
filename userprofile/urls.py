from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('create_profile/', views.ProfileCreate.as_view(), name='create_profile'),
]
