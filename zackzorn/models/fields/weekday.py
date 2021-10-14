# from django.db.models import IntegerField
# 
# class WeekDayField(IntegerField):
# 
#     def __init__(self, *args, **kwargs):
#         kwargs['choices'] = self.DAYS
#         super().__init__(*args, **kwargs)
# 
#     def clean(self, *args, **kwargs):        
#         data = super().clean(*args, **kwargs)
#         try:
#             if data and 0 > data > 6: raise forms.ValidationError(_('Ikke eksisterende '))
#         except AttributeError:
#             pass        
#         return data
