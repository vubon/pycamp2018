from django.urls import path


from . import views


urlpatterns = [
   # path('create/', views.JobPostCreateView.as_view(),name="create"),
    path('', views.JobDashboardView.as_view(),name='jobHome'),
    path('create/',views.JobCreate, name="create"),
]
