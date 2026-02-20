from rest_framework import viewsets, permissions
from .models import Education
from .serializers import EducationSerializer
from core.permissions import IsOwnerOrAdmin


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.select_related('user').all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

