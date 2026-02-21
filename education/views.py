from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Education
from .serializers import EducationSerializer
from .services import EducationService
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
        # We can still validate with serializer, but save via service
        data = serializer.validated_data
        return EducationService.create_education(self.request.user, data, actor=self.request.user)

    def perform_update(self, serializer):
        return EducationService.update_education(serializer.instance, serializer.validated_data, actor=self.request.user)

    def perform_destroy(self, instance):
        EducationService.delete_education(instance, actor=self.request.user)

