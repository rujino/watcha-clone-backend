from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(
        max_length=20,
        default="",
    )
    avator = models.URLField(
        blank=True,
        default="",
    )
    is_adult = models.BooleanField(default=False)


    def __str__(self):
        return self.name
