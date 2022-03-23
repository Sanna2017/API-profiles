from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: #GET is SAFE METHOD
            return True

        # ELSE - update, delete ......
        return obj.id == request.user.id # not checking if AUTH???????????????????
        # will return TRUE or FALSE 

#######################################################

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS: #GET is SAFE METHOD
            return True

        return obj.user_profile.id == request.user.id # not checking if AUTH???????????????????

        # if the object that is being modified has a user_profile.ID same as 
        # the request.user.ID then this will return TRUE and it will allow the permission 
        # through otherwise it will return FALSE and it will block the request being made
