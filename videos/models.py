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
    genre = models.CharField(
        max_length=20,
        default="",
    )
    runtime = models.PositiveIntegerField()
    possible_age = models.CharField(
        max_length=10,
        choices=PossibleAgeChoices.choices,
    )
    director = models.CharField(max_length=20)
    actor = models.CharField(max_length=20)
    episode = models.PositiveIntegerField()
    play_count = models.PositiveIntegerField()
    video_url = models.URLField()
    thumbnail_url = models.URLField()
