from django.urls import path


from . import views


urlpatterns = [
    path('create/', views.EventCreateView.as_view()),
    path('',views.MainDashBoardView.as_view()),
]
