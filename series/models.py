from django.db import models
from common.models import CommonModel


class Series(CommonModel):
    class PossibleAgeChoices(models.TextChoices):
        AGE_all = "all", "All"
        AGE_19 = "19", "19"
        AGE_15 = "15", "15"
        AGE_12 = "12", "12"
        AGE_KIDS = "kids", "Kids"

    title = models.CharField(max_length=100)

    genre = models.ForeignKey(
        "series.Genre",
        max_length=20,
        null=True,
        default="",
        on_delete=models.SET_NULL,
    )

    possible_age = models.CharField(
        max_length=10,
        choices=PossibleAgeChoices.choices,
    )

    director = models.ManyToManyField(
        "series.Director",
        blank=True,
    )

    actor = models.ManyToManyField(
        "series.Actor",
        blank=True,
    )

    summary = models.TextField(
        blank=True,
        null=True,
    )

    poster_url = models.URLField(
        blank=True,
        default="",
    )

    video = models.ManyToManyField("videos.Video", blank=True)

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
