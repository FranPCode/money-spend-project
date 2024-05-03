from django.test import TestCase
from rest_framework import status
from django.core.exceptions import ValidationError

from apps.spends.models import Currency, Spends, Category
from apps.users.models import User


class CurrencyTestCase(TestCase):

    def setUp(self):

        self.currency = Currency.objects.create(
            currency_iso_code='EUR',
            symbol='€'
        )

    def test_unique_data(self):

        with self.assertRaises(ValidationError):
            Currency.objects.create(
                currency_iso_code='EUR',
                symbol='€'
            )

    def test_null_data(self):

        with self.assertRaises(ValidationError):
            Currency.objects.create(
                currency_iso_code=None,
                symbol=None
            )

    def test_null_data2(self):
        with self.assertRaises(ValidationError):
            Currency.objects.create(
                currency_iso_code='aaa',
                symbol=None
            )

    def test_null_data3(self):
        with self.assertRaises(ValidationError):
            Currency.objects.create(
                currency_iso_code=None,
                symbol='AAA'
            )

    def test_null_data4(self):
        with self.assertRaises(ValidationError):
            Currency.objects.create(
                currency_iso_code='AAAA',
                symbol='AAA'
            )

    def test_null_data5(self):
        with self.assertRaises(ValidationError):
            Currency.objects.create(
                currency_iso_code='AAA',
                symbol='aaaaaaaaaa'
            )


class CategoryTestCase(TestCase):

    def setUp(self):

        Category.objects.create(
            name='Donation'
        )

    def test_unique_data(self):

        with self.assertRaises(ValidationError):
            Category.objects.create(
                name='donation'
            )

    def test_null_data(self):

        with self.assertRaises(ValidationError):
            Category.objects.create(
                name=None
            )


class SpendsTestCase(TestCase):

    def setUp(self):

        self.user = User.objects.create(
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

        category = Category.objects.first()
        currency = Currency.objects.first()

        self.spend = Spends.objects.create(
            name='Gasoline for the car',
            description='bought on venezuela avenue',
            amount=50,
            user=self.user,
        )

        self.spend.category.add(category)
        self.spend.currency.add(currency)

    def test_many_to_many_fields(self):

        self.assertTrue(self.spend.currency.exists())
        self.assertTrue(self.spend.category.exists())

    def test_null_data(self):

        with self.assertRaises(ValidationError):
            Spends.objects.create(
                name=None,
                description='bought on venezuela avenue',
                amount=50,
                user=self.user,
            )

    def test_null_data2(self):

        with self.assertRaises(ValidationError):
            Spends.objects.create(
                name='alone',
                description='bought on venezuela avenue',
                amount=None,
                user=self.user,
            )

    def test_null_data3(self):

        with self.assertRaises(ValidationError):
            Spends.objects.create(
                name='test name',
                description='bought on venezuela avenue',
                amount=50,
                user=None,
            )
