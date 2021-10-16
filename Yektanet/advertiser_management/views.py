from .models import *
from django.utils import timezone
from django.views.generic import TemplateView, RedirectView
from django.views.generic.edit import CreateView


class ShowAdsView(TemplateView):
    template_name = 'advertiser_management/ads.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        advertisers = Advertiser.objects.all()
        for advertiser in advertisers:
            advertiser.ads = advertiser.ad_set.filter(approve=True)
            for ad in advertiser.ads:
                View(ad_id=ad, datetime=timezone.now(), ip=self.request.META['REMOTE_ADDR']).save()
        context['advertisers'] = advertisers
        return context


class AdvertiseView(CreateView):
    model = Ad
    fields = ['title', 'img_url', 'link', 'advertiser_id']
    success_url = '/ads/'


class ClickAdView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        ad = Ad.objects.get(pk=kwargs['ad_id'])
        Click(ad_id=ad, datetime=timezone.now(), ip=self.request.META['REMOTE_ADDR']).save()
        return ad.link


class ReportView(TemplateView):
    template_name = 'advertiser_management/total_clicks_views.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ads = Ad.objects.all()
        total = {ad: [] for ad in Ad.objects.all()}
        for i in range(24):
            for ad in ads:
                total[ad].append(
                    (i, i + 1,
                     ad.click_set.filter(datetime__hour=i).count() + ad.view_set.filter(datetime__hour=i).count()))
        context['total'] = total
        rate = {ad: [] for ad in Ad.objects.all()}
        for i in range(24):
            for ad in ads:
                if ad.view_set.filter(datetime__hour=i).count() != 0:
                    rate[ad].append(
                        (i, i + 1,
                         ad.click_set.filter(datetime__hour=i).count() / ad.view_set.filter(datetime__hour=i).count()))
        for ad in ads:
            rate[ad].sort(key=lambda x: -x[2])
        context['rate'] = rate
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
            context['click_delay'] = (click_time - view_time) / view_count
        else:
            context['click_delay'] = 0

        return context
