from rest_framework import authentication
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
)

from .serializers import UserSerializer


class CreateUserView(CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer

create_user_view = CreateUserView.as_view()


class ManageUserView(RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user

manage_user_view = ManageUserView.as_view()
