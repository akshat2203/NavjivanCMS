from django.db import models
from django.conf import settings
from core.storage import UserMediaStorage


def user_media_path(instance, filename):
    # Store per-user to make it easy to produce presigned URLs and lifecycle rules
    return f"users/{instance.user.id}/media/{filename}"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to=user_media_path, null=True, blank=True)
    signature = models.ImageField(upload_to=user_media_path, null=True, blank=True)
    bio = models.TextField(blank=True)

    class Meta:
        indexes = [models.Index(fields=['user'])]

    def __str__(self):
        return f"Profile({self.user_id})"

