from django.db import models
from common.models import CommonModel


class Series(CommonModel):
    class PossibleAgeChoices(models.TextChoices):
        AGE_19 = "19", "19"
        AGE_15 = "15", "15"
        AGE_12 = "12", "12"
        AGE_KIDS = "kids", "Kids"

    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=20)
    possible_age = models.CharField(
        max_length=10,
        choices=PossibleAgeChoices.choices,
    )
    poster_url = models.URLField(
        blank=True,
        default="",
    )

    def __str__(self):
        return self.title
