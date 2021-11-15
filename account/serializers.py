# imports
from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()

# End: imports --------------------------------------------------------------------


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'is_staff',
            'is_superuser',
            'is_active',
            'gender',
            'phone_number',
            'first_name',
            'last_name',
        ]
