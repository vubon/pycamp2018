from django.urls import path


from . import views


urlpatterns = [
    path('', views.MainDashboardView.as_view(), name='dashboard'),
    path('event/create/', views.EventCreateView.as_view(), name="event_create"),
]
