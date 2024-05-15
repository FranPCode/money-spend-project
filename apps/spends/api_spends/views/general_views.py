from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.spends.models import Category, Currency
from apps.spends.api_spends.serializers.general_serializers import CategorySerializer, CurrencySerializer


class CurrencyListCreateAPIView(ListCreateAPIView):

    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


class CategoryListCreateAPIView(ListCreateAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CurrencyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
