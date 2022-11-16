from django.db import models
from common.models import CommonModel


class Wishlists(CommonModel):
    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.SET_NULL,
    )
    video = models.ManyToManyField(
        "videos.Video",
        blank=True,
    )
    list = models.ManyToManyField(
        "lists.List",
    )
