"""User model."""

from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
)
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Custom manager for user model."""

    def create_user(self, username, password, **extra_fields):
        """Create and return an new user."""
        if not username or username == '':
            raise ValueError("The given username must be set")

        if not password or len(password) <= 8:
            raise ValueError(
                "The given password must be set and have 8 or more characters.")

        email = extra_fields.pop('email', '')
        groups = extra_fields.pop('groups', [])
        user_permissions = extra_fields.pop('user_permissions', [])

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        for group in groups:
            user.groups.add(group)

        for perm in user_permissions:
            user.user_permissions.add(perm)

        return user

    def create(self, username, password, **validated_data):
        """Create a user."""
        return self.create_user(
            username=username,
            password=password,
            ** validated_data
        )

    def create_superuser(self, username, password):
        """Create and return a new super user."""
        user = self.create_user(username, password)

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class User(AbstractUser):
    """User Model."""

    objects = CustomUserManager()

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
