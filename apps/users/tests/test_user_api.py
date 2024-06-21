"""Test Users APIs."""

from rest_framework.test import (
    APIClient,
    APITestCase
)
from rest_framework import status

from django.urls import reverse
from django.contrib.auth import get_user_model

USER_URL = reverse('user:user-list')


def detail_url(user_id):
    """Retrieve user."""
    return reverse('user:user-detail', args=[user_id])


class PublicApiTest(APITestCase):
    """Tests for unauthorized users."""

    def setUp(self):
        self.client = APIClient()

    def test_list_unauthorized_request(self):
        """Test unauthorized user request list return error."""
        payload = {
            'username': 'testuser',
            'password': 'testingpass',
        }

        post_response = self.client.post(USER_URL, payload)
        get_response = self.client.get(USER_URL)

        self.assertEqual(post_response.status_code,
                         status.HTTP_201_CREATED)
        self.assertEqual(get_response.status_code,
                         status.HTTP_401_UNAUTHORIZED)

    def test_detail_unauthorized_request(self):
        """Test unauthorized detail request return error."""
        user = get_user_model().objects.create_user(
            username='testusername',
            password='testpassword',
        )

        url = detail_url(user.id)

        retrieve = self.client.get(url)
        patch = self.client.patch(url, {})
        put = self.client.put(url, {})
        delete = self.client.delete(url)

        self.assertEqual(retrieve.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(patch.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(put.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(delete.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateApiTest(APITestCase):
    """Tests for authorized users."""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='usertest',
            password='testingpassword'
        )
        self.client.force_authenticate(self.user)

    def test_create_user(self):
        """Test create a user with post."""
        payload = {
            'username': 'testingpost',
            'password': 'postpassword',
        }
        response = self.client.post(USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_obtain_users_list(self):
        """Test get users list."""
        get_user_model().objects.create_user(
            username='usertestname',
            password='usertestpassword'
        )

        response = self.client.get(USER_URL)

        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_user(self):
        """Test retrieveing a user."""
        user = get_user_model().objects.create_user(
            username='testusername',
            password='testingpassword',
        )
        url = detail_url(user.id)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        """Test update a user."""
        user = get_user_model().objects.create_user(
            username='testusername',
            password='testpasswordd'
        )
        payload = {'email': 'test@email.com'}
        self.client.force_authenticate(user)
        url = detail_url(user.id)
        response = self.client.patch(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        user.refresh_from_db()

        self.assertEqual(user.email, payload['email'])

    def test_delete_user(self):
        """Test delete user."""
        user = get_user_model().objects.create_user(
            username='testusername',
            password='testpassword',
        )
        url = detail_url(user.id)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestTokenView(APITestCase):
    """Tests for token endpoints."""

    def setUp(self):
        self.auth_client = APIClient()
        self.client = APIClient()

        self.user = get_user_model().objects.create(
            username='testusernameee',
            password='paswordtest',
        )
        self.auth_client.force_authenticate(self.user)

        self.obtain_url = reverse('user:token-obtain-pair')
        self.verify_url = reverse('user:token-verify')
        self.refresh_url = reverse('user:token-refresh')

    def test_obtain_token(self):
        """Test unauth user obtain a token."""
        user = {
            'username': 'testusernameee',
            'password': 'paswordtest',
        }

        response = self.client.post(self.obtain_url, user)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)

    def test_verify_token(self):
        """Test verify token is valid."""
        user = {
            'username': 'testusernameee',
            'password ': 'paswordtest',
        }

        response = self.client.post(self.obtain_url, user)
        verify = self.client.post(
            self.verify_url,
            {'token': response.data['access']}
        )

        self.assertEqual(verify.status_code, status.HTTP_200_OK)

    def test_token_refresh(self):
        """Test refresh token successfully."""
        user = {
            'username': 'testusernameee',
            'password': 'paswordtest',
        }

        response = self.client.post(self.obtain_url, user)
        refresh = self.client.post(
            self.refresh_url,
            {'refresh': response.data['refresh']}
        )

        self.assertEqual(refresh.status_code, status.HTTP_200_OK)
        self.assertIn('access', refresh.data)
        self.assertNotEqual(refresh.data['access'], response.data['access'])
