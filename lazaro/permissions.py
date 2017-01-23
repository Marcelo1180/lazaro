from rest_framework.permissions import DjangoModelPermissions
from rest_framework import permissions

# Permisos globales para asignacion dinamica por base de datos en la tabla grupos y Meta.permission en los modelos
class DjangoGuardianModelPermissions(DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.options_%(model_name)s'],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

# class HasGroupPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         user_groups = request.user.groups.values_list('name', flat=True)
#         required_groups = getattr(view, 'required_groups', {})
#         # Return True si alguno de los grupos del usuario estsetan en required_groups
#         if request.user.is_superuser:
#             return True
#         return set(required_groups).intersection(user_groups)
