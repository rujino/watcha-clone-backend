from django.contrib import admin
from .models import Video

# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "genre",
        "runtime",
        "possible_age",
        "director",
        "actor",
        "episode",
        "play_count",
        "video_url",
        "thumbnail_url",
    )
