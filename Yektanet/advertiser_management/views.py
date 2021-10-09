from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Advertiser, Ad
from django.shortcuts import render, redirect
from .forms import AdForm


def show(request):
    advertisers = Advertiser.objects.all()
    for advertiser in advertisers:
        advertiser.inc_views()
        advertiser.save()
        advertiser.ads = advertiser.ad_set.all()
        for ad in advertiser.ads:
            ad.inc_views()
            ad.save()
            ad.advertiser_id.save()
    context = {
        'advertisers': advertisers,
    }
    return render(request, 'advertiser_management/ads.html', context)


def advertise(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            img_url = form.cleaned_data['img_url']
            link = form.cleaned_data['link']
            try:
                advertiser_id = Advertiser.objects.get(pk=form.cleaned_data['advertiser_id'])
            except (KeyError, Advertiser.DoesNotExist):
                return render(request, 'advertiser_management/advertise.html',
                              context={'form': form, 'error_message': 'Advertiser not found!'})
            ad = Ad(title=title, link=link, img_url=img_url, advertiser_id=advertiser_id)
            ad.save()
            return HttpResponseRedirect(reverse('advertiser_management:ads'))
    else:
        form = AdForm()
        return render(request, 'advertiser_management/advertise.html', {'form': form})


def click(request, ad_id):
    ad = Ad.objects.get(pk=ad_id)
    ad.inc_clicks()
    ad.save()
    ad.advertiser_id.save()
    return redirect(ad.link)
