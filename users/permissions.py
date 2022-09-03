from rest_framework import permissions


class SameUserOrReadOnly(permissions.BasePermission):
    """Проверяет, что пользователь совпадает с пользователем запроса или что метод запроса безопасен"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj
