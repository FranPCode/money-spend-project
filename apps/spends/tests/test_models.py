from django.db.utils import IntegrityError, DataError
from django.test import TestCase
from rest_framework import status
from django.core.exceptions import ValidationError

from apps.spends.models import Currency, Spends, Category


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
