# imports
from rest_framework import serializers

from . import models
# End: imports --------------------------------------------------------------------


class ArtistSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = models.Artist
        fields = '__all__'
