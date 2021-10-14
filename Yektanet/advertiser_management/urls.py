from django.urls import path
from . import views

app_name = 'advertiser_management'
urlpatterns = [
    path('advertise/', views.AdvertiseView.as_view(), name='advertise'),
    path('click/<int:ad_id>/', views.ClickAdView.as_view(), name='click'),
    path('ads/', views.ShowAdsView.as_view(), name='show'),
    path('report/', views.ReportView.as_view(), name='Report')
]
