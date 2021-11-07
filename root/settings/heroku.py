from .base import *
import os
import django_heroku

from root.constants import Environment

ALLOWED_HOSTS = ['zackzorn.herokuapp.com']

# Values are set in heroku dashboard
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = eval(os.environ['DEBUG'])

# Ensure correct ENV
ENV = Environment.HEROKU

#  Add configuration for static files storage using whitenoise, heroku
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',  # whitenoise, heroku
]

# activate django-heroku.
django_heroku.settings(locals())
