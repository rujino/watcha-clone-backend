from rest_framework.serializers import ModelSerializer

from coupons.serializer import CouponSerializer
from .models import User


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "avator",
            "username",
        )

class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "username",
        )



class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "name",
            "avator",
            "is_adult",
            "coupon",
            "username",
        )

    coupon = CouponSerializer(
        read_only=True,
        )
