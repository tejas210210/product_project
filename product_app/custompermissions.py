from rest_framework.permissions import BasePermission,SAFE_METHODS


class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_superuser == True:
                return True
            return request.method in SAFE_METHODS
        return False