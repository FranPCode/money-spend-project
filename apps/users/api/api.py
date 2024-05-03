from apps.spends.api_spends.views.general_views import GeneralListAPIView
from apps.users.api.serializer import UserSerializer


class UserAPIView(GeneralListAPIView):

    serializer_class = UserSerializer
