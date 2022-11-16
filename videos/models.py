from django.db import models
from common.models import CommonModel


class Video(CommonModel):
    class PossibleAgeChoices(models.TextChoices):
        AGE_19 = "19", "19"
        AGE_15 = "15", "15"
        AGE_12 = "12", "12"
        AGE_KIDS = "kids", "Kids"

    title = models.CharField(
        max_length=100,
        default="",
    )
    genre = models.ForeignKey(
        "videos.Genre",
        max_length=20,
        null=True,
        default="",
        on_delete=models.SET_NULL,
    )
    runtime = models.PositiveIntegerField()
    possible_age = models.CharField(
        max_length=10,
        choices=PossibleAgeChoices.choices,
    )
    director = models.ManyToManyField(
        "videos.Director",
        blank=True,
    )
    actor = models.ManyToManyField(
        "videos.Actor",
        blank=True,
    )
    episode = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    play_count = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    video_url = models.URLField(
        blank=True,
        default="",
    )
    thumbnail_url = models.URLField(
        blank=True,
        default="",
    )
    series = models.ForeignKey(
        "series.Series",
        null=True,
        max_length=100,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return self.title


class Genre(models.Model):
    genre_name = models.CharField(max_length=20)

    def __str__(self):
        return self.genre_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=20)
    photo_url = models.URLField(
        blank=True,
        default="",
    )

    def __str__(self):
        return self.actor_name


class Director(models.Model):
    director_name = models.CharField(max_length=20)
    photo_url = models.URLField(
        blank=True,
        default="",
    )

    def __str__(self):
        return self.director_name
