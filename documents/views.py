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
        name = self.request.data.get('name')
        if not file_obj:
            from rest_framework import serializers
            raise serializers.ValidationError('file is required')
        doc = DocumentService.validate_and_create(self.request.user, file_obj, name=name, actor=self.request.user)
        serializer.instance = doc
        return doc

    def perform_destroy(self, instance):
        DocumentService.delete_document(instance, actor=self.request.user)
