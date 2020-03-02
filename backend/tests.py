from django.test import Client, TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class user_test(TestCase):
    def setUp(self):
        client = Client()
        User = get_user_model()
        self.test_user = User.objects.get_or_create(
            username="test_user",
            password="password",
            email="admin@admin.com",
        )[0]
        self.client.force_login(self.test_user)

    def test_backend(self):
        response = self.client.get("/backend/")
        self.assertEqual(response.status_code, 200)


    def test_logout(self):
        response = self.client.get("/accounts/logout/")
        self.assertEqual(response.status_code, 200)