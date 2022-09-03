from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
import rest_framework.test as test
import rest_framework.status as status


class UserTestCase(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="TestUser1", password="TestPassword1", is_staff=True)
        self.user2 = User.objects.create_user(username="TestUser2", password="TestPassword2")

    def test_user_detail(self):
        client = test.APIClient()
        client.login(username="TestUser1", password="TestPassword1")

        response = client.get(reverse("user_detail", args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
