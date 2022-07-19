from rest_framework import generics, authentication, permissions, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from user.serializers import UserSerializer, AuthTokenSerialier

from core.models import User


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """Get users list"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for current authenticated user only"""
        return self.queryset.all().order_by('-name')


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer = AuthTokenSerialier
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
