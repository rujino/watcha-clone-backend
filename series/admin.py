from django.contrib import admin
from .models import Series, Genre, Actor, Director


# Register your models here.
@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("genre_name",)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("actor_name",)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("director_name",)