from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHOD:
            return bool(request.user and request.user.is_authenticated)
        return obj.author == request.user
