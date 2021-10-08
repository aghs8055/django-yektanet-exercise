from django.urls import path
from . import views

urlpatterns = [
    path('ads/', views.show, name='ads'),
]
