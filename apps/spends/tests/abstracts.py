from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.spends.models import Currency, Category, Spends
from apps.users.models import User


class RetrieveUpdateDestroyTestCase(APITestCase):

    model = None
    pk = None
    view_url = None
    create_object = None
    patch = None

    def setUp(self):

        if self.view_url:
            self.url = reverse(self.view_url, kwargs={'pk': self.pk})

        self.client = APIClient()

        if self.model == Spends:
            user = User.objects.create(
                username='test',
                email='testing@gmail.com',
                password='testuser',
            )

            Currency.objects.create(
                currency_iso_code='USD',
                symbol='$'
            )

            Category.objects.create(
                name='transport'
            )

            spend = Spends.objects.create(
                name='Gasoline for the car',
                description='bought on venezuela avenue',
                amount=50,
                user=user,
            )

            category = Category.objects.first()
            currency = Currency.objects.first()

            spend.category.add(category)
            spend.currency.add(currency)

        if self.model and self.model != Spends:
            self.model.objects.create(**self.create_object)

    def test_get(self):
        if self.view_url:
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch(self):
        if self.patch:
            data = self.patch
            response = self.client.patch(self.url, data)
            self.assertEqual(response.status_code,
                             status.HTTP_200_OK)

    def test_delete(self):
        if self.view_url:
            response = self.client.delete(self.url)
            self.assertEqual(response.status_code,
                             status.HTTP_204_NO_CONTENT)


class ListCreateTestCase(APITestCase):

    model = None
    view_url = None
    create_object = None
    post = None

    def setUp(self):

        self.client = APIClient()
        if self.view_url:
            self.url = reverse(self.view_url)

        if self.model == Spends:
            user = User.objects.create(
                username='test',
                email='testing@gmail.com',
                password='testuser',
            )

            Currency.objects.create(
                currency_iso_code='USD',
                symbol='$'
            )

            Category.objects.create(
                name='transport'
            )

            spend = Spends.objects.create(
                name='Gasoline for the car',
                description='bought on venezuela avenue',
                amount=50,
                user=user,
            )

            category = Category.objects.first()
            currency = Currency.objects.first()

            spend.category.add(category)
            spend.currency.add(currency)

        if self.model and self.model != Spends:
            self.model.objects.create(**self.create_object)

    def test_post(self):
        if self.post:
            data = self.post
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code,
                             status.HTTP_201_CREATED)

    def test_get(self):
        if self.view_url:
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
