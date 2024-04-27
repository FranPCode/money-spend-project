from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):

    def setUp(self):

        self.currencies_list_url = reverse('api_currencies_all')

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
