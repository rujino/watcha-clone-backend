from rest_framework.serializers import ModelSerializer
from series.serializers import SeriesListSerializer
from .models import List


class ListListSerializer(ModelSerializer):
    class Meta:
        model = List
        fields = (
            "list_name",
            "image_url",
        )


class ListDetailSerializer(ModelSerializer):

    series = SeriesListSerializer()

    class Meta:
        model = List
        fields = (
            "list_name",
            "series",
        )
