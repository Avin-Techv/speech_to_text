from django.db import models

# Create your models here.


class Sound(models.Model):
    description = models.CharField(max_length=255, blank=True)
    sound = models.FileField(upload_to='sounds/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
