from django.db import models
from common.models import CommonModel


# Create your models here.
class Coupon(CommonModel):
    class CouponKindChoices(models.TextChoices):
        PREMIUM = "premium", "Premium"
        BASIC = "basic", "Basic"
        FREE = "free", "Free"
        NONE = "none", "None"

    kind = models.CharField(
        max_length=15,
        choices=CouponKindChoices.choices,
    )
    price = models.PositiveIntegerField()
    HDR = models.BooleanField(default=False)
    quality = models.BooleanField(default=False)
    mobile = models.BooleanField(default=False)
