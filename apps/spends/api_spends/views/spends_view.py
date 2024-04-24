from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView
from apps.spends.api_spends.views.general_views import GeneralListAPIView
from apps.spends.api_spends.serializers.spends_serializers import SpendsSerializer
from apps.spends.models import Spends


class SpendsListAPIView(GeneralListAPIView):

    serializer_class = SpendsSerializer


class SpendsCreateAPIView(CreateAPIView):

    serializer_class = SpendsSerializer


class SpendsRetrieveAPIView(RetrieveAPIView):

    serializer_class = SpendsSerializer
    model = Spends

    def retrieve(self, request, pk=None):
        try:
            model = self.model.objects.get(pk=pk)
            serializer = self.get_serializer(model)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SpendsDestroyAPIView(DestroyAPIView):

    serializer_class = SpendsSerializer
    model = Spends

    def destroy(self, request, pk=None,  *args, **kwargs):

        try:
            model = self.model.objects.get(pk=pk)
            serializer = self.get_serializer(model)
            return Response(
                {
                    "message": "Deleted succesfully",
                    "deleted": serializer.data
                },
                status=status.HTTP_200_OK, )
        except model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
