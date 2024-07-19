"""Views for user API and JWT."""

from rest_framework_simplejwt.views import (
    TokenBlacklistView,
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework_simplejwt.authentication import JWTAuthentication

from drf_yasg.utils import swagger_auto_schema

from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.users.models import User
from apps.users.api.serializer import (
    UserSerializer,
    TokenBlacklistResponseSerializer,
    TokenObtainPairResponseSerializer,
    TokenRefreshResponseSerializer,
    TokenVerifyResponseSerializer
)


class UserListCreateAPIView(generics.ListCreateAPIView):
    """View for creating and listing users."""

    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_permissions(self):
        return (
            [perm() for perm in self.permission_classes]
            if self.request.method != 'POST' else []
        )

    def get_authenticators(self):
        return (
            [auth() for auth in self.authentication_classes]
            if self.request.method != 'POST' else []
        )


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """View for user details."""

    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get_object(self):
        """Return authenticated user."""
        if self.request.user.is_authenticated:
            return self.request.user


class DecoratedTokenObtainPairView(TokenObtainPairView):
    """View for obtaining a new pair of JWT tokens."""
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenRefreshView(TokenRefreshView):
    """Refresh token view."""
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenVerifyView(TokenVerifyView):
    """Verify token view."""
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenVerifyResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenBlacklistView(TokenBlacklistView):
    """Token blacklist view."""
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenBlacklistResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
