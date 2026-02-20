from rest_framework import viewsets, permissions
from .models import AuditLog
from .serializers import AuditLogSerializer


class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuditLog.objects.select_related('actor', 'subject').all().order_by('-created_at')
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        # Admins can filter by subject via query params
        qs = super().get_queryset()
        subject = self.request.query_params.get('subject')
        if subject:
            qs = qs.filter(subject_id=subject)
        return qs

