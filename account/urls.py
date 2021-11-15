# imports
from rest_framework import routers

from django.urls import path, include

from . import views

# End: imports -----------------------------------------------------------------

app_name = 'account'  # Necessary for url naming. eg {% url 'accounts:signin' %}

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
