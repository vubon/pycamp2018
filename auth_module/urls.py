from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('individual_signup/', views.individual_signup, name='individual_signup'),
    path('organization_signup/', views.organization_signup, name='organization_signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('password_change/', views.password_change, name='password_change'),
    path('password_reset/', views.password_reset, name='password_reset'),
]