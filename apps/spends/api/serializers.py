"""Serializers for spends.models"""

from rest_framework import serializers

from apps.spends.models import (
    Spends,
    Category,
    Currency
)
from apps.spends.models import Spends


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category."""
    class Meta:
        model = Category
        fields = ('id', 'name')
        readn_only_fields = ('id',)


class CurrencySerializer(serializers.ModelSerializer):
    """Serialilzer for Currency."""
    class Meta:
        model = Currency
        fields = ('id', 'iso_code', 'symbol')
        read_only_fields = ('id',)


class SpendsSerializer(serializers.ModelSerializer):
    """Serializer for Spends."""

    class Meta:
        model = Spends
        fields = (
            'id',
            'user',
            'title',
            'description',
            'amount',
            'category',
            'currency'
        )
        read_only_fields = ('id',)

    def create(self, validated_data):
        """Create spend serializer."""
        return self.Meta.model.objects.create(**validated_data)
