from django.test import TestCase, SimpleTestCase, Client
from django.urls import resolve, reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from apps.users.api.urls import UserAPIView
from apps.users.models import User


class UserUrlsSimpleTestCase(SimpleTestCase):

    def test_url_users_all(self):

        url = reverse('api_users_all')
        self.assertEqual(resolve(url).func.view_class, UserAPIView)


class UserViewTestCase(TestCase):

    model = User

    def setUp(self) -> None:

        self.client = Client()
        self.users_all_url = reverse('api_users_all')
        self.user = self.model.objects.create(username='ezrealjinx',
                                              password='mitercermatrimonio',
                                              email='vivalavida@gmail.com')

    def test_content(self):

        response = self.client.get(self.users_all_url)
        content_type = response.headers['Content-Type']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(content_type, 'application/json')
        self.assertContains(response, self.user)

    def test_post(self):
        # method not allowed
        response = self.client.post(self.users_all_url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get(self):
        # method allowed
        response = self.client.get(self.users_all_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put(self):
        # method not allowed
        response = self.client.put(self.users_all_url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete(self):
        # method not allowed
        response = self.client.delete(self.users_all_url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)


class UserModelTestCase(TestCase):

    def setUp(self):

        self.user = User.objects.create(
            username='test',
            password='testinguser',
            email='test@gmail.com',
        )

        self.user2 = User(username='test2',
                          email='test2@gmail.com',
                          password='testinguser2'
                          )
        self.user2.save()

    def test_creation(self):

        user_created = User.objects.get(username='test')

        # testing password is tokenize
        self.assertTrue(user_created.password.startswith('pbkdf2_sha256$'))
        self.assertTrue(self.user2.password.startswith('pbkdf2_sha256$'))
