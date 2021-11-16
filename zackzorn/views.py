# imports
from rest_framework import viewsets

from django.views import View
from django.shortcuts import render

from . import models
from . import serializers

# End: imports -----------------------------------------------------------------


class Index(View):
    template = 'zackzorn/index.html'

    def get(self, request):
        return render(request, self.template)


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class = serializers.ArtistSerializer


class MusicGenreViewSet(viewsets.ModelViewSet):
    queryset = models.MusicGenre.objects.all()
    serializer_class = serializers.MusicGenreSerializer
