from rest_framework.serializers import ModelSerializer
from .models import Video


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = (
            "pk",
            "sub_title",
            "episode",
            "runtime",
            "play_count",
            "video_url",
            "thumbnail_url",
        )

class VideoCountSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = (
            "pk",
            "play_count",
        )
    
