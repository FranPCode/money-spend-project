"""URLs for users and JWT."""
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from django.urls import path

from .views import (
    UserListCreateAPIView,
    UserDetailAPIView,
)

app_name = 'user'

urlpatterns = [
    path('user/all/', UserListCreateAPIView.as_view(), name='user-list'),
    path('user/<int:pk>', UserDetailAPIView.as_view(), name='user-detail'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
