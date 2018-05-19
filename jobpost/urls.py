from django.urls import path

from . import views

app_name = 'jobpost'

urlpatterns=[
    path('',views.listView,name='index'),
    path('create/',views.createJobView, name="create"),
    path('detail/<int:id>/',views.detailJobView,name='detail'),
    path('edit/<int:id>/',views.updateView,name='edit'),
    path('delete/<int:id>/',views.deleteView,name='delete'),
    path('apply/<int:id>', views.job_applicant, name='job_apply'),
    path('jobapplicant/', views.JobApplicantListView.as_view(), name='jobapplicant'),
]
