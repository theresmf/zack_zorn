# imports
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core import management
# End: imports -----------------------------------------------------------------

# Settings:
USER_PW = "Django123"


class Command(BaseCommand):

    def f(self):
        from django.conf import settings
        print(settings.SITE_ID)

    def handle(self, *args, **options):
        # management.call_command('show_sites')
        self.f()


        # End of handle
