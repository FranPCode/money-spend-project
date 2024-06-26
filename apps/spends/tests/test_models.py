"""Tests for spends models."""

from decimal import Decimal

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from apps.spends.models import (
    Currency,
    Spends,
    Category
)


class CurrencyTest(TestCase):
    """Tests for currency model."""

    def setUp(self):
        self.currency = Currency.objects.create(
            iso_code='EUR',
            symbol='€'
        )

    def test_unique_data(self):
        """Test currency  attributes must be unique."""

        with self.assertRaises(ValidationError):
            Currency.objects.create(
                iso_code='EUR',
                symbol='€'
            )

    def test_null_data(self):

        with self.assertRaises(ValidationError):
            Currency.objects.create(
                iso_code='TTT',
                symbol=None,
            )

        with self.assertRaises(ValidationError):
            Currency.objects.create(
                iso_code=None,
                symbol='$',
            )

        with self.assertRaises(ValidationError):
            Currency.objects.create(
                iso_code='AAAA',
                symbol='AAA'
            )

    def test_invalid_symbol_error(self):
        """Test invalid symbol return Validation error."""
        with self.assertRaises(ValidationError):
            Currency.objects.create(
                iso_code='AAA',
                symbol='aaaaaaaaaa'
            )

    def test_iso_code_is_upper(self):
        """Test iso code must be upper case."""
        with self.assertRaises(ValidationError):
            Currency.objects.create(
                iso_code='aaa',
                symbol='aaa'
            )

    def test_string_representation(self):
        """Test string representation of currency."""
        self.assertEqual(str(self.currency), self.currency.iso_code)


class CategoryTestCase(TestCase):
    """Tests for category models."""

    def setUp(self):

        self.category = Category.objects.create(
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

    def test_string_representation(self):
        """Test string representation of category."""
        self.assertEqual(str(self.category), self.category.name)


class SpendsTestCase(TestCase):
    """Tests for spend model."""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            password='testusername',
        )
        self.currency = Currency.objects.create(
            iso_code='USD',
            symbol='$'
        )
        self.category = Category.objects.create(
            name='transport'
        )
        self.spend = Spends.objects.create(
            title='Gasoline for the car',
            description='bought on venezuela avenue',
            amount=Decimal('10.99'),
            user=self.user,
            currency=self.currency,
            category=self.category,
        )

    def test_create_spend(self):
        """Test the creation of a new spend."""
        self.assertEqual(str(self.spend), self.spend.title)
        self.assertTrue(self.spend.currency)
        self.assertTrue(str(self.spend.category).istitle())
        # self.assertTrue(str(self.spend).istitle())
