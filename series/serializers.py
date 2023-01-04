from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from videos.serializers import VideoSerializer
from .models import Actor, Director, Genre, Series
from wishlists.models import Wishlist

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"

class DirectorSerializer(ModelSerializer):
    class Meta:
        model = Director
        fields = "__all__"

class SeriesListSerializer(ModelSerializer):
    class Meta:
        model = Series
        fields = (
            "id",
            "title",
            "possible_age",
            "genre",
            "poster_url",
            "is_interested",
        )

    is_interested = serializers.SerializerMethodField()

    genre = GenreSerializer(
        read_only=True,
    )

    def get_is_interested(self, series):
        request = self.context.get("request")
        if request:
            if request.user.is_authenticated:
                return Wishlist.objects.filter(
                    user=request.user,
                    series__pk=series.pk,
                ).exists()
        return False



class SeriesDetailSerializer(ModelSerializer):
    class Meta:
        model = Series
        fields = "__all__"

    video = VideoSerializer(
        read_only=True,
        many=True,
    )

    genre = GenreSerializer(
        read_only=True,
    )

    actor = ActorSerializer(
        read_only=True,
        many=True,
    )

    director = DirectorSerializer(
        read_only=True,
        many=True,
    )


