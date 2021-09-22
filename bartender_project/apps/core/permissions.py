from rest_framework import permissions
from django.utils.translation import gettext_lazy as _


class IsOwner(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        # only owner can get details view data
        return obj.user == request.user


class HasMakeCocktailPermission(permissions.IsAuthenticated):
    message = _('You don not have permission to make a cocktail')

    def has_permission(self, request, view):
        return getattr(request.user.account_type, 'make_cocktail', False)


class HasAddIngredientPermission(permissions.IsAuthenticated):
    message = _('You don not have permission to add an ingredient')

    def has_permission(self, request, view):
        return getattr(request.user.account_type, 'add_ingredient', False)


class HasGenerateLinkPermission(permissions.IsAuthenticated):
    message = _('You don not have permission to generate temporary link')

    def has_permission(self, request, view):
        return getattr(request.user.account_type, 'generate_temp_link', False)
