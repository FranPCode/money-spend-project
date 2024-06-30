"""Tests for spends.api.views."""
from contextlib import AbstractContextManager
from decimal import Decimal
from typing import Any

from rest_framework import status
from rest_framework.test import (
    APIClient,
    APITestCase
)

from django.urls import reverse
from django.contrib.auth import get_user_model


from apps.spends.models import (
    Spends,
    Category,
    Currency
)
from apps.spends.api.serializers import (
    SpendsSerializer,
    CategorySerializer,
    CurrencySerializer,
)
SPEND_URL = reverse('spend:spend-list')
CURRENCY_URL = reverse('spend:currency-list')
CATEGORY_URL = reverse('spend:category-list')


def detail_url(detail_type, id):
    """Retrieve the URL for a specific detail type."""
    return reverse(f'spend:{detail_type}-detail', args=[id])


class PublicSpendTest(APITestCase):
    """Tests for unauthorized requests."""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testingpass',
        )
        self.category = Category.objects.create(
            name='Testcategory'
        )
        self.currency = Currency.objects.create(
            iso_code='USD',
            symbol='$'
        )
        self.spend = Spends.objects.create(
            title='test spend title',
            user=self.user,
            description='Test Spend',
            amount=Decimal('3.99'),
            currency=self.currency,
            category=self.category
        )

    def test_list_create_authorization(self):
        """Tests urls authorization."""
        urls = [SPEND_URL, CURRENCY_URL, CATEGORY_URL]

        for url in urls:
            post = self.client.post(url, {})
            get = self.client.get(url)

            self.assertEqual(post.status_code, status.HTTP_401_UNAUTHORIZED)
            self.assertEqual(get.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_detail_authorization(self):
        """Test detail authorization."""
        spend_detail = detail_url('spend', self.spend.id)
        currency_detail = detail_url('currency', self.currency.id)
        category_detail = detail_url('category', self.category.id)

        urls = [spend_detail, currency_detail, category_detail]
        for url in urls:
            get = self.client.get(url)
            patch = self.client.patch(url, {})
            put = self.client.put(url, {})
            delete = self.client.delete(url)

            self.assertEqual(get.status_code, status.HTTP_401_UNAUTHORIZED)
            self.assertEqual(put.status_code, status.HTTP_401_UNAUTHORIZED)
            self.assertEqual(patch.status_code, status.HTTP_401_UNAUTHORIZED)
            self.assertEqual(delete.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateSpendTest(APITestCase):
    """Tests for authorized users."""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testingpass',
        )
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(
            name='Testcategory'
        )
        self.currency = Currency.objects.create(
            iso_code='USD',
            symbol='$'
        )
        self.spend = Spends.objects.create(
            title='test spend title',
            user=self.user,
            description='Test Spend',
            amount=Decimal('3.99'),
            currency=self.currency,
            category=self.category
        )

    def test_list_create_spend(self):
        """Test list and create spend."""
        payload = {
            'title': 'New Spend',
            'description': 'New Spend Description',
            'amount': '3.99',
            'currency': self.currency.id,
            'category': self.category.id,
            'user': self.user.id
        }
        post = self.client.post(SPEND_URL, payload)
        get = self.client.get(SPEND_URL)

        spends = Spends.objects.all()
        serializer = SpendsSerializer(spends, many=True)

        self.assertEqual(post.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get.status_code, status.HTTP_200_OK)
        self.assertEqual(len(get.data), 2)
        self.assertEqual(get.data, serializer.data)

    def Test_update_spend(self):
        """Test update spend."""
        payload = {'title': 'Updated Spend', }
        url = detail_url('spend', self.spend.id)
        response = self.client.patch(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], payload['title'])

    def test_get_detail_spend(self):
        """Test retrieve detail spend."""
        url = detail_url('spend', self.spend.id)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.spend.title)

    def test_delete_spend(self):
        """Test delete spend."""
        url = detail_url('spend', self.spend.id)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Spends.objects.filter(id=self.spend.id).exists())

    def test_list_create_currency(self):
        """Test list and create currency."""
        payload = {
            'iso_code': 'EUR',
            'symbol': '€',
        }
        post = self.client.post(CURRENCY_URL, payload)
        get = self.client.get(CURRENCY_URL)

        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)

        self.assertEqual(post.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get.status_code, status.HTTP_200_OK)
        self.assertEqual(len(get.data), 2)
        self.assertEqual(get.data, serializer.data)

    def test_update_currency(self):
        """Test update currency."""
        payload = {'iso_code': 'GBP', }
        url = detail_url('currency', self.currency.id)
        response = self.client.patch(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['iso_code'], payload['iso_code'])

    def test_get_detail_currency(self):
        """Test retrieve detail currency."""
        url = detail_url('currency', self.currency.id)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['iso_code'], self.currency.iso_code)

    def test_delete_currency(self):
        """Test delete currency."""
        url = detail_url('currency', self.currency.id)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Currency.objects.filter(id=self.currency.id).exists())

    def test_list_create_category(self):
        """Test list and create category."""
        payload = {
            'name': 'New Category',
        }
        post = self.client.post(CATEGORY_URL, payload)
        get = self.client.get(CATEGORY_URL)

        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        self.assertEqual(post.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get.status_code, status.HTTP_200_OK)
        self.assertEqual(get.data, serializer.data)
        self.assertEqual(len(get.data), 2)

    def test_update_category(self):
        """Test update category."""
        payload = {'name': 'Updated category', }
        url = detail_url('category', self.category.id)
        response = self.client.patch(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], payload['name'])

    def test_get_detail_category(self):
        """Test retrieve detail category."""
        url = detail_url('category', self.category.id)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.category.name)

    def test_delete_category(self):
        """Test delete category."""
        url = detail_url('category', self.category.id)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(id=self.category.id).exists())

    def test_filter_by_currency(self):
        """Test filtering spends by currency."""
        euro = Currency.objects.create(
            iso_code='EUR',
            symbol='€'
        )
        Spends.objects.create(
            title='Euro Spend',
            user=self.user,
            description='Euro Spend Description',
            amount='3.99',
            currency=self.currency,
            category=self.category
        )
        Spends.objects.create(
            title='Euro Spend',
            user=self.user,
            description='Euro Spend Description',
            amount='3.99',
            currency=self.currency,
            category=self.category
        )
        Spends.objects.create(
            title='Euro Spend',
            user=self.user,
            description='Euro Spend Description',
            amount='3.99',
            currency=euro,
            category=self.category
        )
        response = self.client.get(SPEND_URL, {'currency': self.currency.id})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_filter_by_category(self):
        """Test filtering spends by category."""
        transport = Category.objects.create(
            name='Transport'
        )
        Spends.objects.create(
            title='Euro Spend',
            user=self.user,
            description='Euro Spend Description',
            amount='3.99',
            currency=self.currency,
            category=self.category
        )
        Spends.objects.create(
            title='Euro Spend',
            user=self.user,
            description='Euro Spend Description',
            amount='3.99',
            currency=self.currency,
            category=self.category
        )
        Spends.objects.create(
            title='Euro Spend',
            user=self.user,
            description='Euro Spend Description',
            amount='3.99',
            currency=self.currency,
            category=transport
        )

        response = self.client.get(SPEND_URL, {'category': transport.id})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
