# imports
from django import template
from django.conf import settings
# End: imports -----------------------------------------------------------------

register = template.Library()

# https://docs.djangoproject.com/en/3.0/howto/custom-template-tags/

@register.inclusion_tag('zackzorn/components/screen.html')
def screen_component(screen, *args, **kwargs):
    default_classes = ''
    return {
        'screen': screen,
        'classes': kwargs.get('classes', default_classes),
    }
