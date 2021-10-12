from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.shortcuts import render, redirect
from .forms import AdForm
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
