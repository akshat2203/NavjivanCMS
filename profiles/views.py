from rest_framework import viewsets, permissions
from .models import Profile
from .serializers import ProfileSerializer
from core.permissions import IsOwnerOrAdmin


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.select_related('user').all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Admins see all, users see only their profile
        if self.request.user.is_staff:
            return self.queryset
        return self.queryset.filter(user=self.request.user)

