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


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
