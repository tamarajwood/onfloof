from rest_framework import permissions 

class IsAdminUserOrReadOnly(permissions.BasePermission):

    def has_premission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or 
            request.user.username == 'tjwood'
        )

class AdminReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.username == 'tjwood'

class PostOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or 
            request.method == 'POST'
        )
