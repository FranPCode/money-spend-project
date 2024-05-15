from django.test import SimpleTestCase
from django.urls import reverse, resolve

from apps.spends.api_spends.views import spends_view, general_views
from apps.spends.models import Spends, Category, Currency
from apps.spends.tests.abstracts import RetrieveUpdateDestroyTestCase, ListCreateTestCase


class SpendsUrlsSimpleTestCase(SimpleTestCase):

    def setUp(self):

        self.spends_lc_url = reverse('api_spends_list_create')
        self.spends_rud_url = reverse(
            'api_spends_retrieve_update_destroy', kwargs={'pk': 1})

        self.currencies_lc_url = reverse('api_currencies_list_create')
        self.currencies_rud_url_url = reverse(
            'api_currencies_retrieve_update_destroy', kwargs={'pk': 1})

        self.categories_lc_urls = reverse('api_categories_list_create')
        self.categories_rud_urls = reverse(
            'api_categories_retrieve_update_destroy', kwargs={'pk': 1})

    def test_spends_urls(self):

        self.assertEqual(resolve(self.spends_lc_url).func.view_class,
                         spends_view.SpendsListCreateAPIView)
        self.assertEqual(resolve(self.spends_rud_url).func.view_class,
                         spends_view.SpendsRetrieveUpdateDestroyAPIView)

    def test_currencies_urls(self):

        self.assertEqual(resolve(self.currencies_lc_url).func.view_class,
                         general_views.CurrencyListCreateAPIView)
        self.assertEqual(resolve(self.currencies_rud_url_url).func.view_class,
                         general_views.CurrencyRetrieveUpdateDestroyAPIView)

    def test_categories_urls(self):

        self.assertEqual(resolve(self.categories_lc_urls).func.view_class,
                         general_views.CategoryListCreateAPIView)
        self.assertEqual(resolve(self.categories_rud_urls).func.view_class,
                         general_views.CategoryRetrieveUpdateDestroyAPIView)


class SpendsLCTestCase(ListCreateTestCase):

    model = Spends
    view_url = 'api_spends_list_create'
    post = {
        'name': 'testing spending',
        'amount': 125,
        'currency': [1,],
        'category': [1, ],
        'user': 1,
    }


class SpendsRUDTestCase(RetrieveUpdateDestroyTestCase):

    model = Spends
    pk = 1
    view_url = 'api_spends_retrieve_update_destroy'
    post = {
        'name': 'spending testing',
        'amount': 12345,
        'currency': 1,
        'category': 1,
        'user': 1,
    }
    patch = {'name': 'hello testing'}


class CurrencyLCTestCase(ListCreateTestCase):

    model = Currency
    view_url = 'api_currencies_list_create'
    create_object = {'currency_iso_code': 'TSS', 'symbol': 'S/.'}
    post = {'currency_iso_code': 'EEE', 'symbol': '$'}


class CurrencyRUDTestCase(RetrieveUpdateDestroyTestCase):

    model = Currency
    pk = 1
    view_url = 'api_currencies_retrieve_update_destroy'
    create_object = {'currency_iso_code': 'TST', 'symbol': '$'}
    post = {'Currency_iso_code': 'TXT', 'symbol': '€'}
    patch = {'currency_iso_code': 'TTT'}


class CategoryLCTestCase(ListCreateTestCase):

    model = Category
    view_url = 'api_categories_list_create'
    create_object = {'name': 'Administration'}
    post = {'name': 'Testing'}


class CategoryRUDTestCase(RetrieveUpdateDestroyTestCase):

    model = Category
    pk = 1
    view_url = 'api_categories_retrieve_update_destroy'
    create_object = {'name': 'Testing'}
    post = {'name': 'Testeando'}
    patch = {'name': 'Test'}
