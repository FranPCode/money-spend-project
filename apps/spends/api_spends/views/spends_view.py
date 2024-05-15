from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.spends.api_spends.serializers.spends_serializers import SpendsSerializer
from apps.spends.models import Spends


class SpendsListCreateAPIView(ListCreateAPIView):

    serializer_class = SpendsSerializer
    queryset = Spends.objects.all()


class SpendsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = SpendsSerializer
    queryset = Spends.objects.all()
