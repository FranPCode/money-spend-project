from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            # "date_joined",
            # "last_login",
            "is_active",
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions",
        ]

    def create(self, validated_data):

        groups_data = validated_data.pop('groups', [])
        user_permissions_data = validated_data.pop('user_permissions', [])
        password = validated_data.pop('password')

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        user.groups.set(groups_data)
        user.user_permissions.set(user_permissions_data)

        return user

    def update(self, instance, validated_data):

        updated_user = super().update(instance, validated_data)
        if 'password' in validated_data.keys():
            updated_user.set_password(validated_data['password'])

        updated_user.save()

        return updated_user
