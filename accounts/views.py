from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .services import UserService


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterSerializer
        return UserSerializer

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def me(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

