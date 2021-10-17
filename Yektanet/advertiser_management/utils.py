from .models import *


def get_report():
    report = {}
    ads = Ad.objects.all()
    total = {ad: [] for ad in Ad.objects.all()}
    for i in range(24):
        for ad in ads:
            total[ad].append(
                (i, i + 1,
                 ad.click_set.filter(datetime__hour=i).count() + ad.view_set.filter(datetime__hour=i).count()))
    report['total_clicks_views'] = total
    rate = {ad: [] for ad in Ad.objects.all()}
    for i in range(24):
        for ad in ads:
            if ad.view_set.filter(datetime__hour=i).count() != 0:
                rate[ad].append(
                    (i, i + 1,
                     ad.click_set.filter(datetime__hour=i).count() / ad.view_set.filter(datetime__hour=i).count()))
    for ad in ads:
        rate[ad].sort(key=lambda x: -x[2])
    report['click_rate'] = rate
    views = View.objects.all()
    click_time, view_time, view_count = 0, 0, 0
    for view in views:
        click_times = []
        view_time += view.datetime.timestamp()
        clicks = Click.objects.filter(ad_id=view.ad_id, datetime__gt=view.datetime, ip=view.ip)
        for click in clicks:
            click_times.append(click.datetime.timestamp())
        if len(click_times) != 0:
            click_time += sum(click_times) / len(click_times)
            view_count += 1
        else:
            view_time -= view.datetime.timestamp()
    if len(views) != 0:
        report['click_delay'] = (click_time - view_time) / view_count
    else:
        report['click_delay'] = 0
    return report
