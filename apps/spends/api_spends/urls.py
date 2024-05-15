from django.urls import path
from apps.spends.api_spends.views.general_views import CategoryListCreateAPIView, CategoryRetrieveUpdateDestroyAPIView, CurrencyListCreateAPIView, CurrencyRetrieveUpdateDestroyAPIView
from apps.spends.api_spends.views.spends_view import SpendsListCreateAPIView, SpendsRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('currencies/all/', CurrencyListCreateAPIView.as_view(),
         name='api_currencies_list_create'),
    path('currencies/<int:pk>/', CurrencyRetrieveUpdateDestroyAPIView.as_view(),
         name='api_currencies_retrieve_update_destroy'),
    path('categories/all/', CategoryListCreateAPIView.as_view(),
         name='api_categories_list_create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(),
         name='api_categories_retrieve_update_destroy'),
    path('spends/all/', SpendsListCreateAPIView.as_view(),
         name='api_spends_list_create'),
    path('spends/<int:pk>/', SpendsRetrieveUpdateDestroyAPIView.as_view(),
         name='api_spends_retrieve_update_destroy'),
]
