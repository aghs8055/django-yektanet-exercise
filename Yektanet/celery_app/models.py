from django.db import models
from django.utils import timezone
from advertiser_management.models import Ad


class HourReport(models.Model):
    year = models.IntegerField(null=False)
    month = models.IntegerField(null=False)
    day = models.IntegerField(null=False)
    hour = models.IntegerField(null=False)
    clicks = models.IntegerField()
    views = models.IntegerField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)


class DayReport(models.Model):
    year = models.IntegerField(null=False)
    month = models.IntegerField(null=False)
    day = models.IntegerField(null=False)
    clicks = models.IntegerField()
    views = models.IntegerField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
