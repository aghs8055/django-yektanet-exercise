from rest_framework import serializers
from Yektanet.advertiser_management.models import *


class AdvertiserSerializer(serializers.ModelSerializer):
    class META:
        model = Advertiser


class AdSerializer(serializers.ModelSerializer):
    class META:
        model = Ad


class ViewSerializer(serializers.ModelSerializer):
    class META:
        model = View


class ClickSerializer(serializers.ModelSerializer):
    class META:
        model = Click
