from django.urls import path


from . import views


urlpatterns = [
    path('', views.JobDashboardView.as_view(),name='jobHome'),
    path('joblist/', views.JobListView.as_view(),name='joblist'),
    path('create/',views.JobCreate, name="create"),
    path('job/<int:pk>', views.JobDetailView.as_view(), name='job_post_detail'),
    path('delete/<int:pk>', views.JobDeleteView.as_view(), name='job_post_delete'),
    path('apply/<int:pk>', views.job_applicant, name='job_apply'),
    path('jobapplicant/', views.JobApplicantListView.as_view(), name='jobapplicant'),


]