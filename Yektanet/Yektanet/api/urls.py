from django.urls import path
from . import views

urlpatterns = [
    path('ads/', views.AdView.as_view()),
    path('advertise/', views.CreateAdView.as_view()),
    path('click/', views.CreateClickView.as_view()),
    path('report/', views.ReportView.as_view())
]
