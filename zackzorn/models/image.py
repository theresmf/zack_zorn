from django.db import models

from root import models as root_models

class Image(root_models.CustomBaseModel):
    name = models.CharField(max_length=140, null=True, blank=True)
    url = models.URLField(null=False, blank=False)
    
    def __str__(self):
        return f"{self.name}"