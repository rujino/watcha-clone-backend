from django.contrib import admin
from .models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = (
        "kind",
        "price",
        "HDR",
        "quality",
        "mobile",
    )
