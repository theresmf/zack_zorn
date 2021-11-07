from django.contrib import admin

# from root import models as root_models
from . import models as zackzorn_models


@admin.register(zackzorn_models.MusicGenre)
class MusicGenre(admin.ModelAdmin):
    list_display = ['name']
    # ordering = []
    # list_filter = []
    # filter_horizontal = []
    search_fields = ['name']


@admin.register(zackzorn_models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'artist_name', 'age']
    ordering = ['last_name']
    # list_filter = []
    # filter_horizontal = []
    search_fields = ['first_name', 'last_name', 'artist_name']


@admin.register(zackzorn_models.Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    list_filter = ['genre']
    filter_horizontal = ['genre', 'members']
    search_fields = ['name']


@admin.register(zackzorn_models.Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'band', 'release_date', 'producer', 'price']
    ordering = ['title']
    list_filter = ['genre']
    filter_horizontal = ['genre', 'featuring']
    search_fields = ['title', 'band__title', 'producer']


@admin.register(zackzorn_models.Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['title', 'album', 'length']
    ordering = ['title']
    # list_filter = []
    filter_horizontal = ['featuring']
    search_fields = ['title', 'album__title']


@admin.register(zackzorn_models.BookGenre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    # ordering = []
    # list_filter = []
    # filter_horizontal = []
    search_fields = ['name']


@admin.register(zackzorn_models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']
    ordering = ['title']
    # list_filter = []
    filter_horizontal = ['genre']
    search_fields = ['title']
