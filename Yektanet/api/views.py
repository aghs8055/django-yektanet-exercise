from rest_framework import generics
from rest_framework import views
from . import serializers
from rest_framework.response import Response
from advertiser_management.models import *
import advertiser_management
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.utils import timezone


class AdView(generics.ListAPIView):
    serializer_class = serializers.AdSerializer

    def get_queryset(self):
        ads = Ad.objects.filter(approve=True)
        for ad in ads:
            View(ad_id=ad, datetime=timezone.now(), ip=self.request.META.get('REMOTE_ADDR', None)).save()
        return ads


class CreateAdView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.AdSerializer


class CreateClickView(generics.CreateAPIView):
    serializer_class = serializers.ClickSerializer


class ReportView(views.APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAdminUser]

    def get(self, request):
        context = advertiser_management.views.ReportView().get_context_data()
        ads = Ad.objects.all()
        response = {'ad_' + str(ad.id): {
            'total_clicks_views': context['total'][ad],
            'click_rate': context['rate'][ad],
            'click_delay': context['click_delay']
        } for ad in ads}
        response['click_delay'] = context['click_delay']
        return Response(response)
