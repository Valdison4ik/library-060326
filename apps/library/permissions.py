from django.contrib.auth.models import PermissionsMixin
from rest_framework.permissions import BasePermission, SAFE_METHODS, DjangoModelPermissions


class CanGetStatistics(BasePermission):
    message = 'You are not allowed to get statistics'
    def has_permission(self, request, view):
        user = request.user

        return user.has_perm('library.can_get_statistic')





class StrictDjangoModelPermissions(DjangoModelPermissions):
    perms_map = {
        **DjangoModelPermissions.perms_map,
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
    }


class IsLibrarian(BasePermission):
    message = 'You are not librarian'

    def has_permission(self, request, view):
        user = request.user

        if not (user and user.is_authenticated):
            return False
        return user.has_role('staff')


class IsBorrowedOrLibrarian(BasePermission):
    message = 'You are not borrow this book'

    def has_object_permission(self, request, view, obj):
        user = request.user
        if not (user and user.is_authenticated):
            return False

        return user.has_role('staff') or user.pk == obj.member.pk





