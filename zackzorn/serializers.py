# imports
from rest_framework import serializers

from . import models
# End: imports --------------------------------------------------------------------


class ArtistSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = models.Artist
        fields = '__all__'


class MusicGenreSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = models.MusicGenre
        fields = '__all__'


class BandSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = models.Band
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = models.Album
        fields = '__all__'
