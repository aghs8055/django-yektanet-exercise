from django.db import models
from django.utils import timezone
from advertiser_management.models import Ad


class HourReport(models.Model):
    year = models.IntegerField(default=(timezone.now() - timezone.timedelta(hours=1)).year)
    month = models.IntegerField(default=(timezone.now() - timezone.timedelta(hours=1)).month)
    day = models.IntegerField(default=(timezone.now() - timezone.timedelta(hours=1)).day)
    hour = models.IntegerField(default=(timezone.now() - timezone.timedelta(hours=1)).hour)
    clicks = models.IntegerField()
    views = models.IntegerField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)


class DayReport(models.Model):
    year = models.IntegerField(default=(timezone.now() - timezone.timedelta(days=1)).year)
    month = models.IntegerField(default=(timezone.now() - timezone.timedelta(days=1)).month)
    day = models.IntegerField(default=(timezone.now() - timezone.timedelta(days=1)).day)
    clicks = models.IntegerField()
    views = models.IntegerField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
