from django.urls import path
from apps.spends.api_spends.views.general_views import CurrencyListAPIView, CategoryListAPIView
from apps.spends.api_spends.views.spends_view import SpendsListAPIView, SpendsCreateAPIView, SpendsRetrieveAPIView, SpendsDestroyAPIView
urlpatterns = [
    path('currencies/all/', CurrencyListAPIView.as_view(),
         name='api_currencies_all'),
    path('categories/all', CategoryListAPIView.as_view(),
         name='api_categories_all'),
    path('spends/all/', SpendsListAPIView.as_view(),
         name='api_spends_all'),
    path('create/spends', SpendsCreateAPIView.as_view(),
         name='api_create_spends'),
    path('spends/<int:pk>/', SpendsRetrieveAPIView.as_view(),
         name='api_retrieve_spends'),
    path('destroy/spends/<int:pk>', SpendsDestroyAPIView.as_view(),
         name='api_destroy_spends'),
]
