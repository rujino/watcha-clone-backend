from django.db import models
from common.models import CommonModel


class Wishlist(CommonModel):
    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.CASCADE,
    )
    series = models.ManyToManyField(
        "series.Series",
        blank=True,
    )
