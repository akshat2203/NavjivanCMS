from rest_framework import viewsets, permissions, status
from .models import Document
from .services import DocumentService
from .serializers import DocumentSerializer
from core.permissions import IsOwnerOrAdmin
from rest_framework.response import Response


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset.select_related('user')
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # serializer.validated_data contains no file; handle via request.FILES
        file_obj = self.request.FILES.get('file')
        if not file_obj:
            raise serializers.ValidationError('file is required')
        doc = DocumentService.validate_and_create(self.request.user, file_obj)
        serializer.instance = doc
        return doc
