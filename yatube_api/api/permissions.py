from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class ReadOnlyAndIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            and request.user.is_authenticated
        )
