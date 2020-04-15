from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from unittest.mock import patch
from models.models import *


# Create your tests here.
class todo_list_test(TestCase):
    def setUp(self):
        client = Client()
        user = get_user_model()
        self.test_user = user.objects.get_or_create(username="test_user", password="password")[0]
        self.client.force_login(self.test_user)

    def test_create_list(self):
        """ test that verifies that a user can create a list """
        __author__ = "Alex Hicks"
        response = self.client.get('/dashboard/create_list/')
        self.assertEqual(response.status_code, 200)

    def test_create_list2(self):
        """ test that verifies that a user can create a list """
        __author__ = "Alex Hicks"
        data = {'task_user': self.test_user, 'task_list_name': 'task_list', 'task_list_description': 'nope'}
        response = self.client.post('/dashboard/create_list/', data)
        self.assertRedirects(response, '/dashboard/todo/')

    def test_create_item(self):
        """ test that verifies that a user can create an item """
        __author__ = "Alex Hicks"
        response = self.client.get('/dashboard/create_item/')
        self.assertEqual(response.status_code, 200)

    def test_update_list(self):
        """ test that verifies that a user can update a list """
        __author__ = "Alex Hicks"
        pass

    def test_update_item(self):
        """ test that verifies that a user can update an item """
        __author__ = "Alex Hicks"
        pass

    def test_check_todo(self):
        """ test that verifies that a user can see the todo view """
        __author__ = "Alex Hicks"
        response = self.client.get('/dashboard/todo/')
        self.assertEqual(response.status_code, 200)

    def test_delete_list(self):
        """ test that verifies that a user can delete a list """
        __author__ = "Alex Hicks"
        response = self.client.get('/dashboard/delete_list/')
        self.assertRedirects(response, '/dashboard/dashboard/')

    def test_delete_item(self):
        """ test that verifies that a user can delete an item """
        __author__ = "Alex Hicks"
        response = self.client.get('/dashboard/delete_item/')
        self.assertRedirects(response, '/dashboard/dashboard/')

    def test_view_list(self):
        """ test that verifies that a user can view a list """
        __author__ = "Alex Hicks"
        response = self.client.get('/dashboard/view_lists/')
        self.assertEqual(response.status_code, 200)

    def test_view_items(self):
        """ test that verifies that a user can view the list items """
        __author__ = "Alex Hicks"
        response = self.client.get('/dashboard/view_items/')
        self.assertEqual(response.status_code, 200)

    def test_view_completed_items(self):
        """ test that verifies that a user can view the completed list items """
        __author__ = "Alex Hicks"
        response = self.client.get('/dashboard/view_completed_items/')
        self.assertEqual(response.status_code, 200)

    def test_grade_calc(self):
        response = self.client.get('/dashboard/grade_calc/')
        self.assertEqual(response.status_code, 200)

    def test_calendar(self):
        response = self.client.get('/dashboard/calendar/')
        self.assertEqual(response.status_code, 200)

    def test_invalid(self):
        response = self.client.get('/dashboard/view_list')
        self.assertEqual(response.status_code, 404)
