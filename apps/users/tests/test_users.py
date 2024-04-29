from django.test import TestCase, SimpleTestCase, Client
from django.urls import resolve, reverse
from django.utils import timezone

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

        response = self.client.get(self.users_all_url)
        content_type = response.headers['Content-Type']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(content_type, 'application/json')
        self.assertContains(response, self.user)

    def test_post(self):
        # method not allowed
        response = self.client.post(self.users_all_url)
        self.assertEqual(response.status_code, 405)

    def test_get(self):
        # method allowed
        response = self.client.get(self.users_all_url)
        self.assertEqual(response.status_code, 200)

    def test_put(self):
        # method not allowed
        response = self.client.put(self.users_all_url)
        self.assertEqual(response.status_code, 405)

    def test_delete(self):
        # method not allowed
        response = self.client.delete(self.users_all_url)
        self.assertEqual(response.status_code, 405)
        # usar django.http.status


class TestUserModel(TestCase):

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

        self.assertEqual(self.user.username, user_created.username)
        self.assertEqual(self.user.email, user_created.email)
        self.assertEqual(self.user.password, user_created.password)

        # testing correct date
        self.assertLess(self.user.date_joined, timezone.now())

        # testing password is tokenize
        self.assertTrue(user_created.password.startswith('pbkdf2_sha256$'))
        self.assertTrue(self.user2.password.startswith('pbkdf2_sha256$'))

        # testear cosas que tu creas
        # no testear el framework
        # hacer clases de autocracion de modelos
