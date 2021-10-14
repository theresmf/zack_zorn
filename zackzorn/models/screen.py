from django.db import models
from root import models as root_models


class Screen(root_models.CustomBaseModel):
    name = models.CharField(max_length=140, unique=True, null=True, blank=True)
    slug = models.CharField(max_length=140, unique=True, null=False, blank=False)
    
    # images = models.ManyToManyField('Image', through='ScreenHasImage')
    images = models.ManyToManyField('infoscreen.Image', blank=True)
    
    def __str__(self):
        return f"{self.name}"
    

# class ScreenHasImage(models.Model):
#     screen = models.ForeignKey('infoscreen.Screen', on_delete=models.CASCADE, null=False, blank=False)
#     image = models.ForeignKey('infoscreen.Image', on_delete=models.CASCADE, null=False, blank=False)
#     nr = models.IntegerField(null=False, blank=False)
# 
#     class Meta:
#         unique_together = ['screen', 'image']
