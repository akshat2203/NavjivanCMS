from django.db import models
from django.conf import settings
from django.utils import timezone

# Sensitive fields: store encrypted blob in BinaryField and store last4 separately for masking

class Aadhaar(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='aadhaar')
    encrypted = models.BinaryField(null=True, editable=False)
    last4 = models.CharField(max_length=4, db_index=True)
    issued_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=['user', 'last4'])]

    def masked(self):
        return f"XXXX-XXXX-{self.last4}"


class PAN(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pan')
    encrypted = models.BinaryField(null=True, editable=False)
    last4 = models.CharField(max_length=4, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=['user', 'last4'])]

    def masked(self):
        # PAN usually alphanumeric; mask except last 4
        return f"XXXX-XXXX-{self.last4}"

