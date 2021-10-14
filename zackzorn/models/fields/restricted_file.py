from django.db.models import FileField


class ContentTypeRestrictedFileField(FileField):
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
"""
    def __init__(self, content_types=None, max_upload_size=5242880,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.content_types = content_types
        self.max_upload_size = max_upload_size

    def clean(self, *args, **kwargs):        
        data = super().clean(*args, **kwargs)

        file = data.file
        try:
            content_type = file.content_type
            if content_type in self.content_types:
                if file._size > self.max_upload_size:
                    raise forms.ValidationError(_('Hold filestørrelsen under %s. Nåværende filstørrelse %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
            else:
                raise forms.ValidationError(_('Filetype ikke støttet.'))
        except AttributeError:
            pass        

        return data