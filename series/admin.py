from django.contrib import admin
from .models import Series

# Register your models here.
@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "genre",
        "possible_age",
    )
