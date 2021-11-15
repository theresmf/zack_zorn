# imports
from django.db import models
from django.contrib.auth import models as auth_models
# End: imports -----------------------------------------------------------------


class User(auth_models.AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        OTHER = 'O', 'Other'

    gender = models.CharField(max_length=1, choices=Gender.choices, default=None, null=True, blank=True)
    phone_number = models.CharField(max_length=13, default=None, null=True, blank=True)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return f'{self.get_full_name() or self.username or self.email or self.id}'
