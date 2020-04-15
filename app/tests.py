from django.test import Client, TestCase

# Create your tests here.
class todo_list_test(TestCase):
    def setUp(self):
        client = Client()

    def test_create_list(self):
        """ test that verifies that a user can create a list """
        __author__ = "Alex Hicks"
        pass

    def test_create_item(self):
        """ test that verifies that a user can create an item """
        __author__ = "Alex Hicks"
        pass

    def test_update_list(self):
        """ test that verifies that a user can update a list """
        __author__ = "Alex Hicks"
        pass

    def test_update_item(self):
        """ test that verifies that a user can update an item """
        __author__ = "Alex Hicks"
        pass

    def test_delete_list(self):
        """ test that verifies that a user can delete a list """
        __author__ = "Alex Hicks"
        pass

    def test_delete_item(self):
        """ test that verifies that a user can delete an item """
        __author__ = "Alex Hicks"
        pass

    def test_view_list(self):
        """ test that verifies that a user can view a list """
        __author__ = "Alex Hicks"
        pass

    def test_view_items(self):
        """ test that verifies that a user can view the list items """
        __author__ = "Alex Hicks"
        pass
