# imports
from rest_framework import routers

from django.urls import include, path

from . import views
# End: imports ------------------------------------------------

app_name = 'zackzorn'

ROUTER = routers.DefaultRouter()
ROUTER.register('api/artists', views.ArtistViewSet)
ROUTER.register('api/music-genres', views.MusicGenreViewSet)
ROUTER.register('api/bands', views.BandViewSet)

urlpatterns = [
    path('', include(ROUTER.urls)),
]
