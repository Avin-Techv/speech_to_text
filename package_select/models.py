from django.db import models

# Create your models here.

INPUT_METHOD = (
    ('upload', 'UPLOAD FILE'),
    ('record', 'RECORD'),
)

RECOGNITION_PACKAGE = (
    ('bing', 'Microsoft Bing Speech'),
    ('google', 'Google Web Speech API'),
    ('google_cloud', 'Google Cloud Speech'),
    ('houndify', 'Houndify'),
    ('ibm', 'IBM Speech to Text'),
    ('sphinx', ' CMU Sphinx'),
    ('wit', 'Wit.ai'),
)


class Sound(models.Model):
    input_method = models.CharField(choices=INPUT_METHOD, default='upload', max_length=255)
    document = models.FileField(upload_to='documents/')
    recognition_package = models.CharField(choices=RECOGNITION_PACKAGE, default='upload', max_length=255)
