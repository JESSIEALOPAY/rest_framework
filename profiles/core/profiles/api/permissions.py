from rest_framework import permissions
from pprint import pprint

class ProfileOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS :
            return True
        # print("----------")
        # pprint(request.content_type)
        # print("----------")
        # pprint("request: ",request.method)
        # pprint("obj: ",obj)
        return request.user == obj.user


class ProfileStatusOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.profile == obj.user_profile



