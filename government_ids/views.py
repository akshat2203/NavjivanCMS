from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import AadhaarSerializer, PANSerializer
from core.permissions import IsOwnerOrAdmin
from .services import GovernmentIDService
from django.shortcuts import get_object_or_404

User = get_user_model()


class AadhaarViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def retrieve(self, request, pk=None):
        # Support: GET /api/v1/aadhaar/me/  or /api/v1/aadhaar/<user_id>/ for admins
        if pk in (None, 'me'):
            target_user = request.user
        else:
            # non-admins may only fetch their own
            if str(request.user.id) == str(pk) or request.user.is_staff:
                target_user = get_object_or_404(User, pk=pk)
            else:
                return Response({'detail': 'forbidden'}, status=status.HTTP_403_FORBIDDEN)

        masked = GovernmentIDService.get_masked_aadhaar(target_user)
        return Response({'masked': masked})

    def create(self, request):
        # body: {"aadhaar": "123412341234", "issued_at": "YYYY-MM-DD"}
        aadhaar = request.data.get('aadhaar')
        issued_at = request.data.get('issued_at')
        if not aadhaar:
            return Response({'detail': 'aadhaar is required'}, status=status.HTTP_400_BAD_REQUEST)
        obj = GovernmentIDService.set_aadhaar(request.user, aadhaar, issued_at=issued_at, actor=request.user)
        return Response({'id': obj.id, 'masked': obj.masked()}, status=status.HTTP_201_CREATED)


class PANViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def retrieve(self, request, pk=None):
        if pk in (None, 'me'):
            target_user = request.user
        else:
            if str(request.user.id) == str(pk) or request.user.is_staff:
                target_user = get_object_or_404(User, pk=pk)
            else:
                return Response({'detail': 'forbidden'}, status=status.HTTP_403_FORBIDDEN)

        masked = GovernmentIDService.get_masked_pan(target_user)
        return Response({'masked': masked})

    def create(self, request):
        pan = request.data.get('pan')
        if not pan:
            return Response({'detail': 'pan is required'}, status=status.HTTP_400_BAD_REQUEST)
        obj = GovernmentIDService.set_pan(request.user, pan, actor=request.user)
        return Response({'id': obj.id, 'masked': obj.masked()}, status=status.HTTP_201_CREATED)
