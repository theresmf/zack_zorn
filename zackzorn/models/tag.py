# imports
import re

from django.db import models
from django.db.models import Q
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

from root import models as root_models

# End: imports -----------------------------------------------------------------

        
class Tag(root_models.CustomBaseModel):
    name = models.CharField(max_length=200, unique=True, null=False, blank=False, verbose_name='navn', help_text="En vilkårlig egenskap til en plante. (Tips: Du kan prefikse tags med kolon ':', f.eks. 'familie:fiola' )")
    bg = models.ForeignKey('infoscreen.Color', on_delete=models.SET_NULL, null=True, blank=True, related_name='tag_bg', verbose_name='bakgrunnsfarge')
    font = models.ForeignKey('infoscreen.Color', on_delete=models.SET_NULL, null=True, blank=True, related_name='tag_font', verbose_name='skriftfarge')
    group = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children', verbose_name='gruppe')
    
    class Meta:
        ordering = []
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        
    def __str__(self):
        return f"{self.full_name()}"
        
    def full_name(self):
        if self.group:
            return f"{self.group.full_name()} :: {self.name}"
        return f"{self.name}"
    
    
    def color_list(self):
        """Hierarchical list of colors from least to most significant"""
        colors = []
        if self.tag_group:
            colors += self.tag_group.color_list()
        if self.color:
            colors.append(self.color)
        return colors
    
    def color_list_css(self):
        return [color.as_css() for color in self.color_list()]
            
    