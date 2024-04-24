from rest_framework import serializers
from apps.spends.models import Spends


class SpendsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Spends
        fields = '__all__'

    def to_representation(self, instance):

        instance_id = instance.id

        category_instance = instance.category.get(spends=instance_id)
        currency_instance = instance.currency.get(spends=instance_id)

        return {
            "id": instance.id,
            "user": {
                "id": instance.user.id,
                "username": instance.user.username
            },
            "name": instance.name,
            "description": instance.description,
            "category": category_instance.name,
            "amount": instance.amount,
            "currency": {
                "currency_iso_code": currency_instance.currency_iso_code,
                "symbol": currency_instance.symbol,
            },
            "date_created": instance.date_created,
        }
