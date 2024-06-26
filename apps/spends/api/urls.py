"""URLs for spends."""

from django.urls import path
from apps.spends.api.views import (
    SpendsListCreateAPIView,
    CategoryListCreateAPIView,
    CurrencyListCreateAPIView,
    SpendsDetailAPIView,
    CategoryDetailAPIView,
    CurrencyDetailAPIView,
)

app_name = 'spend'

urlpatterns = [
    path('currencies/all/', CurrencyListCreateAPIView.as_view(), name='currency-list'),
    path('currencies/<int:pk>/', CurrencyDetailAPIView.as_view(),
         name='currency-detail'),
    path('categories/all/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(),
         name='category-detail'),
    path('spends/all/', SpendsListCreateAPIView.as_view(), name='spend-list'),
    path('spends/<int:pk>/', SpendsDetailAPIView.as_view(), name='spend-detail'),
]
