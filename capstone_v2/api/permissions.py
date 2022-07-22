from rest_framework import permissions 

class IsAdminUserOrReadOnly(permissions.BasePermission):

    def has_premission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or 
            request.user.username == 'tjwood'
        )

class AdminReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.username == 'tjwood'