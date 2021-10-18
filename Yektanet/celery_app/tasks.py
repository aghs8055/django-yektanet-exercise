from celery import task
from advertiser_management import Ad
from django.db.models import Count, Q
from django.utils import timezone

hourly_reports = []
daily_reports = []


@task
def create_hourly_report():
    global hourly_reports
    hourly_report = Ad.objects.all().annotate(
        clicks=Count('click', filter=Q(click__datetime__hour=timezone.now().hour - 1)))
    hourly_report = hourly_report.annotate(views=Count('click', filter=Q(view__datetime__hour=timezone.now().hour - 1)))
    hourly_reports.append(hourly_report)
    return hourly_report


@task
def create_daily_report():
    global hourly_reports
    global daily_reports
    daily_report = {ad: {'clicks': 0, 'views': 0} for ad in Ad.objects.all()}
    if len(hourly_reports) >= 24:
        last_hours = hourly_reports[-24:]
    else:
        last_hours = hourly_reports
    for ad in Ad.objects.all():
        for hour in last_hours:
            daily_report[ad]['clicks'] += hour.get(pk=ad.pk).clicks
            daily_report[ad]['vies'] += hour.get(pk=ad.pk).views
    daily_reports.append(daily_report)
    return daily_report
