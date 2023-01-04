from rest_framework.serializers import ModelSerializer

from series.serializers import SeriesListSerializer
from .models import Wishlist


class WishlistsSerializer(ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"
    
    series = SeriesListSerializer(
        read_only=True,
        many=True,
        )
