"""Tests for user."""

from django.test import TestCase
from django.contrib.auth import get_user_model


class UserModelTestCase(TestCase):
    """Tests for user model."""

    def test_create_user(self):
        """Test the creation of a user."""
        password = 'testpassword'

        user = get_user_model().objects.create_user(
            username='test',
            password=password
        )

        self.assertTrue(user.check_password(password))

    def test_creation_with_email(self):
        """Test the creation of a user with cleaned emaill."""
        email = 'test@Email.Com'

        user = get_user_model().objects.create_user(
            username='testusername',
            password='testpassword',
            email=email,
        )

        self.assertTrue(user.email.endswith('@email.com'))

    def test_create_superuser(self):
        """Test the creation of a superuser."""

        superuser = get_user_model().objects.create_superuser(
            username='testname',
            password='testingpass',
        )

        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_no_username_or_password_raise_error(self):
        """Test raises an error if username or password is not passed."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create(
                username='',
                password='testpass',
            )

        with self.assertRaises(ValueError):
            get_user_model().objects.create(
                username=None,
                password='testpass',
            )

        with self.assertRaises(ValueError):
            get_user_model().objects.create(
                username='testname',
                password='',
            )

        with self.assertRaises(ValueError):
            get_user_model().objects.create(
                username='testuser',
                password=None,
            )

    def test_no_username_or_password_raise_error_create_user(self):
        """Test raises an error if username or password is not passed."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                username='',
                password='testpass',
            )

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                username=None,
                password='testpass',
            )

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                username='testname',
                password='',
            )

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                username='testuser',
                password=None,
            )
