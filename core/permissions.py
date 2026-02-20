from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Allow full access to admins, read-only to others."""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.is_staff


class IsOwnerOrAdmin(permissions.BasePermission):
    """Allow object modifications only to owner or admin."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and (request.user.is_staff or getattr(obj, 'user_id', None) == request.user.id or getattr(obj, 'user', None) == request.user)

