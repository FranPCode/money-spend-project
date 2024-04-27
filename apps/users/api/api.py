from rest_framework import status
from rest_framework.response import Response

from apps.spends.api_spends.views.general_views import GeneralListAPIView
from apps.users.api.serializer import UserSerializer, User


class UserAPIView(GeneralListAPIView):

    serializer_class = UserSerializer
