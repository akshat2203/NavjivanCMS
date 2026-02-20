from django.db import models
from django.conf import settings


class AuditLog(models.Model):
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='actor_logs')
    subject = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='subject_logs')
    action = models.CharField(max_length=128)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['actor']), models.Index(fields=['subject']), models.Index(fields=['action'])]

    def __str__(self):
        return f"{self.created_at} {self.actor} {self.action}"

