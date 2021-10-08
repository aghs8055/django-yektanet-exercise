from django.http import HttpResponse
from django.template import loader
from .models import Ad


def show(request, ad_id):
    template = loader.get_template('advertiser_management/templates/advertiser_management/ads.html')
    ad = Ad.objects.get(pk=ad_id)
    context = {
        'ad': ad,
        'advertiser': ad.advertiser_id,
    }
    return HttpResponse(template.rander(context, request))
