from django.test import Client, TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class login_test(TestCase):
    def setUp(self):
        client = Client()

    def test_get_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_home_authenticated(self):
        user = get_user_model()
        self.test_user = user.objects.get_or_create(username="test_user", password="password")[0]
        self.client.force_login(self.test_user)
        response = self.client.get('/')
        self.assertRedirects(response, '/dashboard/dashboard/')

    def test_get_dashboard(self):
        response = self.client.get('/dashboard/dashboard')
        self.assertTemplateNotUsed(response, 'dashboard.html')

    def test_get_dashboard_authenticated(self):
        user = get_user_model()
        self.test_user = user.objects.get_or_create(username="test_user", password="password")[0]
        self.client.force_login(self.test_user)
        response = self.client.get('/dashboard/dashboard/')
        self.assertTemplateUsed(response, 'dashboard.html')
