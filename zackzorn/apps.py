from django.apps import AppConfig


class InfoScreenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'zackzorn'
    
    def ready(self):
        
        from django.core import management
        
        try:
            # https://docs.djangoproject.com/en/3.0/ref/django-admin/#createsuperuser
            management.call_command('createsuperuser', interactive=False)
        except:
            pass
