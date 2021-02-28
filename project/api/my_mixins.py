from rest_framework import permissions


class PermMixin:
    permission_classes = [permissions.IsAuthenticated]