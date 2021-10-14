# imports
import os
import glob

from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand

# End: imports -----------------------------------------------------------------


class Command(BaseCommand):

    def handle(self, *args, **options):
        for app in settings.INSTALLED_APPS:
            
            appname = app.split('.')[-1]
            
            try:
                management.call_command('makemigrations', appname)

            except Exception as e:
                pass
                print(f"{app} failed. {e}")
