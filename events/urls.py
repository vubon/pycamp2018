from django.urls import path


from . import views


urlpatterns = [
    path('', views.MainDashboardView.as_view(), name='dashboard'),
    path('create/', views.EventCreateView.as_view(), name="event_create"),
    path('archive/', views.EventArchiveView.as_view(), name="event_archive"),
    path('profile/', views.OrganizerProfileVew.as_view(), name="organizer_profile"),
]
