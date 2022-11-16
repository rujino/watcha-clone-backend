from django.contrib import admin
from .models import Video, Genre, Actor, Director

# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "genre",
        "runtime",
        "possible_age",
        "episode",
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("genre_name",)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("actor_name",)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("director_name",)
