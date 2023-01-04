from rest_framework.serializers import ModelSerializer
from users.serializers import TinyUserSerializer
from .models import Review


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

    user = TinyUserSerializer(read_only=True,)
