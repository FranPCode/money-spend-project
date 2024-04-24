from rest_framework.generics import ListAPIView

from apps.spends.models import Category, Currency
from apps.spends.api_spends.serializers.general_serializers import CategorySerializer, CurrencySerializer


class GeneralListAPIView(ListAPIView):

    serializer_class = None

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.all()


class CurrencyListAPIView(GeneralListAPIView):

    serializer_class = CurrencySerializer


class CategoryListAPIView(GeneralListAPIView):

    serializer_class = CategorySerializer
