from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('advertiser/', include('advertiser_management.urls')),
    path('admin/', admin.site.urls),
]
