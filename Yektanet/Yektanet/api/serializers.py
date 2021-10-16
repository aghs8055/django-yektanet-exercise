from rest_framework import serializers
from advertiser_management.models import *
from django.utils import timezone


class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = ['ad_id']


class ClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Click
        fields = ['ad_id']

    def create(self, validated_data):
        return Click.objects.create(**validated_data, datetime=timezone.now(), ip=self.request.META['REMOTE_ADDR'])
