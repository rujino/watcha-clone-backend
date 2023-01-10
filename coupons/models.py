from django.db import models
from common.models import CommonModel



# Create your models here.
class Coupon(CommonModel):

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
