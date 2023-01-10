from django.utils import timezone
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Coupon

class CouponSerializer(ModelSerializer):

    class Meta:
        model = Coupon
        fields = ("__all__")

