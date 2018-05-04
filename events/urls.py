from django.urls import path


from . import views


urlpatterns = [
    path('', views.MainDashboardView.as_view()),
    path('event/create/', views.EventCreateView.as_view()),
]
