from django.db import models
from django.conf import settings
from core.storage import UserMediaStorage


def marksheet_upload_path(instance, filename):
    return f"users/{instance.user.id}/education/{filename}"


class Education(models.Model):
    LEVEL_CHOICES = [
        ('ssc', 'SSC'),
        ('hsc', 'HSC'),
        ('graduation', 'Graduation'),
        ('post_graduation', 'Post Graduation'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='educations')
    level = models.CharField(max_length=32, choices=LEVEL_CHOICES)
    board = models.CharField(max_length=255)
    passing_year = models.PositiveSmallIntegerField(db_index=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    marksheet = models.FileField(upload_to=marksheet_upload_path, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['user', 'level']), models.Index(fields=['passing_year'])]

    def __str__(self):
        return f"{self.user_id} - {self.level} - {self.passing_year}"

