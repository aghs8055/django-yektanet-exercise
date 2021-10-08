from django.http import HttpResponse
from django.template import loader
from .models import Advertiser


def show(request):
    template = loader.get_template('advertiser_management/templates/advertiser_management/ads.html')
    advertisers = Advertiser.objects.all()
    context = {
        'advertisers': advertisers,
    }
    return HttpResponse(template.rander(context, request))
