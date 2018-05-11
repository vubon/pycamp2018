from django.urls import path


from . import views


urlpatterns = [
    path('create_profile/', views.create_profile, name='create_profile'),
]