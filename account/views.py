# imports
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet

from . import serializers

User = get_user_model()

# End: imports -----------------------------------------------------------------


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
