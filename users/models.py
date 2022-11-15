from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(
        max_length=150,
        editable=False,
        null=True,
        blank=True,
        default="",
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
        null=True,
        blank=True,
        default="",
    )
    name = models.CharField(
        max_length=20,
        default="",
    )
    avator = models.URLField(blank=True)
    is_adult = models.BooleanField(default=False)
    coupon = models.ForeignKey(
        "coupons.Coupon",
        max_length=15,
        null=True,
        on_delete=models.SET_NULL,
    )
    avator = models.URLField(blank=True)
