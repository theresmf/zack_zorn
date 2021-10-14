from django.db import models

from root import models as root_models


class Color(root_models.CustomBaseModel):
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='navn')
    hex = models.CharField(max_length=6, null=True, blank=True, verbose_name="hex", help_text="Fargekode i hex (6 symboler)")

    class Meta:
        ordering = []
        verbose_name = 'farge'
        verbose_name_plural = 'farger'
        
    def __str__(self):
        return f"{self.get_name()}"
    
    def get_name(self):
        if self.name:
            return self.name
        return self.hex
    
    def as_css(self):
        # TODO: handle COLOR_RANDOM
        # if self.name == root_constants.COLOR_RANDOM:
        #     return 
        return f"#{self.hex}"
    
    def clean(self, *args, **kwargs):
        super().clean(*args, **kwargs)
        errors = {}
        if self.hex:
            if not re.search('^[0-9a-f]+$', self.hex, flags=re.IGNORECASE):
                errors['hex'] = 'Ugyldig format. Bruk 0-9 og A-F'
        if errors:
            raise ValidationError(errors)
    
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
