from celery import shared_task
from advertiser_management.models import Ad
from django.db.models import Count, Q, Sum
from .models import *
from django.utils import timezone


@shared_task(name='hourly_report')
def create_hourly_report():
    print(2)
    hour_report = []
    date = timezone.now() - timezone.timedelta(hours=1)
    year, month, day, hour = date.year, date.month, date.day, date.hour
    ads = Ad.objects.all().annotate(clicks=Count('click', filter=Q(click__datetime__year=year) and Q(
        click__datetime__month=month) and Q(click__datetime__day=day) and Q(click__datetime__hour=hour)))
    ads = ads.annotate(views=Count('click', filter=Q(view__datetime__year=year) and Q(
        view__datetime__month=month) and Q(view__datetime__day=day) and Q(view__datetime__hour=hour)))
    for ad in ads:
        ad_report = HourReport(clicks=ad.clicks, views=ad.views, ad=ad)
        ad_report.save()
        hour_report.append(ad_report)
    return hour_report


@shared_task(name='daily_report')
def create_daily_report():
    print(1)
    day_report = []
    date = timezone.now() - timezone.timedelta(days=1)
    year, month, day, hour = date.year, date.month, date.day, date.hour
    ads = Ad.objects.all()
    for ad in ads:
        clicks = HourReport.objects.filter(ad=ad, year=year, month=month, day=day).aggregate(Sum('clicks'))[
            'clicks__sum']
        views = HourReport.objects.filter(ad=ad, year=year, month=month, day=day).aggregate(Sum('views'))[
            'views__sum']
        ad_report = DayReport(ad=ad, clicks=clicks, views=views)
        ad_report.save()
        day_report.append(ad_report)
    return day_report

