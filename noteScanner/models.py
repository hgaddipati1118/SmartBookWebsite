from django.db import models

# models.py
actionOptions= [
    ('uploadText', 'Upload as Text'),
    ('uploadFile', 'Upload as File'),
    ('translate', 'Translate Text'),
    ('uploadTranslate', 'Upload Translated Text'),
    ('readText', 'Read Text Out Loud'),
    ('readTextUpload', "Read Text Out Loud and Then Upload Recording"),
     ('readTranslation', 'Read Translation Out Loud'),
     ('readTranslationUpload', "Read Translation Out Loud and Then Upload Recording")
    ]
class Image(models.Model):
    action = models.CharField(max_length=30, choices=actionOptions, default = "uploadFile")
    main_Img = models.ImageField(upload_to='static/noteScanner/input/')