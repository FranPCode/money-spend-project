"""URLs for users and JWT."""

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from django.urls import path

from .views import (
    UserListCreateAPIView,
    UserDetailAPIView,
    CustomTokenObtainPairView
)

app_name = 'user'

urlpatterns = [
    path('user/all/', UserListCreateAPIView.as_view(), name='user-list'),
    path('user/<int:pk>', UserDetailAPIView.as_view(), name='user-detail'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
