from django.test import TestCase, SimpleTestCase, Client
from django.urls import resolve, reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from apps.users.api.urls import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView
from apps.users.models import User


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


class UserUrlsSimpleTestCase(SimpleTestCase):

    def test_url_list_create(self):

        url = reverse('api_users_list_create')
        self.assertEqual(resolve(url).func.view_class,
                         UserListCreateAPIView)

    def test_url_retrieve_update_destroy(self):

        url = reverse('api_user_retrieve_update_destroy', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class,
                         UserRetrieveUpdateDestroyAPIView)


class UserListCreateAPIViewTestCase(APITestCase):

    model = User

    def setUp(self) -> None:

        self.client = APIClient()
        self.users_url = reverse('api_users_list_create')
        self.user = self.model.objects.create(username='ezrealjinx',
                                              password='mitercermatrimonio',
                                              email='vivalavida@gmail.com')

    def test_content(self):

        response = self.client.get(self.users_url)
        content_type = response.headers['Content-Type']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(content_type, 'application/json')
        self.assertContains(response, self.user)

    def test_get(self):
        # method allowed
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        # method allowed
        user = {
            'username': 'testeando1234',
            'email': 'testeando@gmail.com',
            'password': 'testeandopost'
        }

        response = self.client.post(self.users_url, user)
        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED)

    def test_put(self):
        # method not allowed
        response = self.client.put(self.users_url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete(self):
        # method not allowed
        response = self.client.delete(self.users_url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)


class UserRetrieveUpdateDestroyAPIViewTestCase(APITestCase):

    model = User

    def setUp(self) -> None:

        self.client = APIClient()
        self.user = self.model.objects.create(username='ezrealjinx',
                                              password='mitercermatrimonio',
                                              email='vivalavida@gmail.com')

        self.users_url = reverse('api_user_retrieve_update_destroy',
                                 kwargs={'pk': 1})

    def test_content(self):

        response = self.client.get(self.users_url)
        content_type = response.headers['Content-Type']

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(content_type, 'application/json')
        self.assertContains(response, self.user)

    def test_get(self):
        # method allowed
        response = self.client.get(self.users_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post(self):
        # method not allowed
        response = self.client.post(self.users_url)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_patch(self):
        # method allowed
        user_patch = {'username': 'testingpatch'}
        response = self.client.patch(self.users_url, user_patch, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK)

        user_updated = self.model.objects.get(pk=1)
        self.assertEqual(user_patch['username'], user_updated.username)

    def test_delete(self):
        # method allowed
        response = self.client.delete(self.users_url)
        self.assertEqual(response.status_code,
                         status.HTTP_204_NO_CONTENT)
