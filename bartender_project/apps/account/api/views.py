from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .serializers import UserSerializer


class CreateUserView(CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer

create_user_view = CreateUserView.as_view()


class ManageUserView(RetrieveUpdateDestroyAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user

    def destroy(self, request, *args, **kwargs):
        """Delete a user ,setting is_active=False"""
        request.user.is_active = False
        request.user.save()
        content = {"result" : "User deleted successfully"}
        return Response(content, status=204)

manage_user_view = ManageUserView.as_view()
