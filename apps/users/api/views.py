from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from apps.users.api.serializer import UserSerializer
from apps.users.models import User


class UserListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = UserSerializer
    queryset = User.objects.all()
