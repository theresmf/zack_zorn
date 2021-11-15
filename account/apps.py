from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'account'

    def ready(self):

        from django.core import management
        from django.core.management.base import CommandError
        try:
            management.call_command('createsuperuser', interactive=False)
        except (ValueError, CommandError) as e:
            print(f'=== {__file__} ===')
            print(f'management.call_command(\'createsuperuser\', interactive=False)')
            print(f'=>\t{str(e)}\n')
