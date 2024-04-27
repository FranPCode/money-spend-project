from django.urls import path
from rest_framework.decorators import APIView
from .api import UserAPIView

urlpatterns = [
    path('users/all/', UserAPIView.as_view(), name='api_users_all'),
]
