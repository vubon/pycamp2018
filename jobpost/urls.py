from django.urls import path


from . import views


urlpatterns = [
    path('', views.JobDashboardView.as_view(),name='jobHome'),
    path('joblist/', views.JobListView.as_view(),name='joblist'),
    path('create/',views.JobCreate, name="create"),
]