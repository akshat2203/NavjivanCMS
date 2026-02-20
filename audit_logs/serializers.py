from rest_framework import serializers
from .models import AuditLog


class AuditLogSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    subject = serializers.StringRelatedField()

    class Meta:
        model = AuditLog
        fields = ('id', 'actor', 'subject', 'action', 'message', 'created_at')

