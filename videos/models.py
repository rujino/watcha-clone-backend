from django.db import models
from common.models import CommonModel


class Video(CommonModel):
    sub_title = models.CharField(
        max_length=100,
        default="",
    )
    
    episode = models.PositiveIntegerField(
        blank=True,
        null=True,
        default=1,
    )

    runtime = models.PositiveIntegerField()

    play_count = models.PositiveIntegerField(
        default=0,
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

    def __str__(self):
        return self.sub_title
