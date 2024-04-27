from django.test import TestCase, SimpleTestCase, Client
from django.urls import resolve, reverse

from apps.users.api.urls import UserAPIView
from apps.users.models import User


class TestUserUrls(SimpleTestCase):

    def test_url_users_all(self):

        url = reverse('api_users_all')
        self.assertEqual(resolve(url).func.view_class, UserAPIView)


class TestUserView(TestCase):

    model = User

    def setUp(self) -> None:

        self.client = Client()
        self.users_all_url = reverse('api_users_all')
        self.user = self.model.objects.create(username='ezrealjinx',
                                              password='mitercermatrimonio',
                                              email='vivalavida@gmail.com')

    def test_content(self):

        client = self.client
        response = client.get(self.users_all_url)
        content_type = response.headers['Content-Type']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(content_type, 'application/json')
        self.assertContains(response, self.user)
