from rest_framework import generics
from rest_framework import views
from . import serializers
from rest_framework.response import Response
from advertiser_management.models import *
import advertiser_management


class AdView(generics.ListAPIView):
    serializer_class = serializers.AdSerializer

    def get_queryset(self):
        ads = Ad.objects.filter(approve=True)
        for ad in ads:
            View(ad_id=ad, datetime=timezone.now(), ip=self.request.META['REMOTE_ADDR'])
        return ads


class CreateAdView(generics.CreateAPIView):
    serializer_class = serializers.AdSerializer


class CreateClickView(generics.CreateAPIView):
    serializer_class = serializers.ClickSerializer


class ReportView(views.APIView):
    def get(self, request):
        context = advertiser_management.views.ReportView().get_context_data()
        ads = Ad.objects.all()
        response = {'ad_'+str(ad.id): {
            'total_clicks_views': context['total'][ad],
            'click_rate': context['rate'][ad],
            'click_delay': context['click_delay']
        } for ad in ads}
        response['click_delay'] = context['click_delay']
        return Response(response)
