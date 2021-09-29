from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # What should be returned in api response
        # data['username'] = self.user.username
        # data['email'] = self.user.email

        serializer = UserSerializer(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CreateUserView(CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer

    # def post(self, request, *args, **kwargs):
    #     serializer = UserSerializer(data=request.data)
    #     data = {}
    #     if serializer.is_valid():
    #         user = serializer.save()
    #         data['response'] = 'Successfully registered a new user!'
    #         data['email'] = user.email
    #         data['username'] = user.username
    #         data['token'] = serializer.get_token(user)
    #         new_user = authenticate(username=request.POST.get('username'),
    #             password=request.POST.get('password'),
    #             )
    #         if new_user is not None and new_user.is_active:
    #             login(request, new_user)
    #     else:
    #         data = serializer.errors
    #     return Response(data, status=status.HTTP_201_CREATED)

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
