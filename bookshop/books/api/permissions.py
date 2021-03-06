from rest_framework import permissions


# class IsAdminOrReadOnly(permissions.IsAdminUser):
#         def has_permission(self, request, view):
#             is_admin = super().has_permission(request,view)
#             return request.method in permissions.SAFE_METHODS or is_admin



class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        # return super().has_permission(request, view)
        return bool(request.method in permissions.SAFE_METHODS or (request.user and request.user.is_staff))



class IsCommentOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user== obj.commenter :
            return True
        else:
            return False

