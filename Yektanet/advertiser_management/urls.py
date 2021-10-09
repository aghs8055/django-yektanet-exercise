from django.urls import path
from . import views

app_name = 'advertiser_management'
urlpatterns = [
    path('ads/', views.show, name='ads'),
    path('advertise/', views.advertise, name='advertise'),
    path('click/<int:ad_id>/', views.click, name='click'),
]
