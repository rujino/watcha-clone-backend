from django.db import models
from common.models import CommonModel



# Create your models here.
class Coupon(CommonModel):
    username = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.username
