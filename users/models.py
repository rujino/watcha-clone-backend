from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(
        max_length=20,
        blank=True,
        default="",
    )
    avator = models.URLField(
        blank=True,
        default="",
    )
    is_adult = models.BooleanField(default=False)
    coupon = models.ForeignKey(
        "coupons.Coupon",
        max_length=15,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
