from .base import *

import os

from root.constants import Environment

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = True

# Ensure correct ENV
ENV = Environment.DEV

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
