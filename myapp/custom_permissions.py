from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "admin"

class IsLead(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "lead"

class IsEmployee(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "employee"
