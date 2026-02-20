from django.db import models
from django.conf import settings
from core.storage import UserS3Storage


def document_upload_path(instance, filename):
    return f"users/{instance.user.id}/documents/{filename}"


class Document(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='documents')
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=document_upload_path)
    content_type = models.CharField(max_length=128)
    size = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['user']), models.Index(fields=['created_at'])]

    def __str__(self):
        return f"Document({self.name})"

