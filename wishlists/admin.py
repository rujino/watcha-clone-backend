from django.contrib import admin
from wishlists.models import Wishlists

# Register your models here.
@admin.register(Wishlists)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("user",)
