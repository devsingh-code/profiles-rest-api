from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    '''Allows user to edit only their profile and not other profiles'''

    def has_object_permission(self,request,view,obj):
        '''Check user is trying to edit their own profile'''
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
