from django.db import models
from common.models import CommonModel

# Create your models here.
class Review(CommonModel):
    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.SET_NULL,
    )
    series = models.ForeignKey(
        "series.Series",
        null=True,
        on_delete=models.SET_NULL,
    )
    text = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.text
