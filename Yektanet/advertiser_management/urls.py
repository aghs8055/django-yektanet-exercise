from django.urls import path
from . import views

urlpatterns = [
    path('ad/<int:ad_id>', views.show, name='show'),
]
