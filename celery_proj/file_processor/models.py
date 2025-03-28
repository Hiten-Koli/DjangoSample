from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    processed = models.BooleanField(default=False)
    result_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
