from django.db import models
from common.models import CommonModel


class List(CommonModel):
    list_name = models.CharField(max_length=50)
    series = models.ManyToManyField(
        "series.Series",
        blank=True,
    )
    image_url = models.URLField(
        blank=True,
        default="",
    )
