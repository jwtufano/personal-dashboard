from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from unittest.mock import patch
from models.models import *
from .forms import *
from datetime import datetime, timedelta

class todo_list_urls_test(TestCase):
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

    def test_check_todo(self):
        """ test that verifies that a user can see the todo view """
        __author__ = "Alex Hicks"
        response = self.client.get('/dashboard/todo/')
        self.assertEqual(response.status_code, 200)

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

    def test_calendar(self):
        response = self.client.get('/dashboard/calendar/')
        self.assertEqual(response.status_code, 200)

    def test_invalid(self):
        response = self.client.get('/dashboard/view_list')
        self.assertEqual(response.status_code, 404)

class todo_list_test(TestCase):
    def setUp(self):
        client = Client()
        user = get_user_model()
        self.test_user = user.objects.get_or_create(username="test_user", password="password")[0]
        self.client.force_login(self.test_user)
        self.test_prof = Profile.objects.get(user=self.test_user)

    def test_create_list(self):
        before_num_lists = TaskList.objects.count()
        TaskList.objects.create(task_user=self.test_prof, task_list_name="test_create_list")
        test_list = TaskList.objects.get(task_list_name="test_create_list")
        self.assertEqual(before_num_lists+1, TaskList.objects.count())
        

    def test_delete_list(self):
        before_num_lists = TaskList.objects.count()
        TaskList.objects.create(task_user=self.test_prof, task_list_name="test_delete_list")
        test_list = TaskList.objects.get(task_list_name="test_delete_list")
        test_list.delete()
        self.assertEqual(before_num_lists, TaskList.objects.count())
        self.assertRaises(TaskList.DoesNotExist, TaskList.objects.get, task_list_name="test_delete_list")

    def test_list___str__(self):
        TaskList.objects.create(task_user=self.test_prof, task_list_name="test_list___str__")
        test_list = TaskList.objects.get(task_list_name="test_list___str__")
        self.assertEqual(test_list.task_list_name, test_list.__str__())

    def test_create_item(self):
        before_num_items = TaskItem.objects.count()
        TaskList.objects.create(task_user=self.test_prof, task_list_name="test_create_item")
        test_list = TaskList.objects.get(task_list_name="test_create_item")
        TaskItem.objects.create(task_name="test_create_item", task_list=test_list)
        test_item = TaskItem.objects.get(task_name="test_create_item")
        self.assertEqual(before_num_items+1, TaskItem.objects.count())
        
    def test_delete_item(self):
        before_num_items = TaskItem.objects.count()
        TaskList.objects.create(task_user=self.test_prof, task_list_name="test_delete_item")
        test_list = TaskList.objects.get(task_list_name="test_delete_item")
        TaskItem.objects.create(task_name="test_delete_item", task_list=test_list)
        test_item = TaskItem.objects.get(task_name="test_delete_item")
        test_item.delete()
        self.assertEqual(before_num_items, TaskItem.objects.count())
        self.assertRaises(TaskItem.DoesNotExist, TaskItem.objects.get, task_name="test_delete_item")

    def test_item_edit_name(self):
        TaskList.objects.create(task_user=self.test_prof, task_list_name="test_item_edit_name")
        test_list = TaskList.objects.get(task_list_name="test_item_edit_name")
        TaskItem.objects.create(task_name="test_item_edit_name", task_list=test_list)
        test_item = TaskItem.objects.get(task_name="test_item_edit_name")
        test_item.edit_name("test_item_edit_name_edited")
        self.assertEqual(test_item.task_name, "test_item_edit_name_edited")

    def test_item_edit_description(self):
        TaskList.objects.create(task_user=self.test_prof, task_list_name="test_item_edit_description")
        test_list = TaskList.objects.get(task_list_name="test_item_edit_description")
        TaskItem.objects.create(task_name="test_item_edit_description", task_list=test_list)
        test_item = TaskItem.objects.get(task_name="test_item_edit_description")
        test_item.edit_description("test_item_edit_description_edited")
        self.assertEqual(test_item.task_description, "test_item_edit_description_edited")

    def test_item_edit_due_date(self):
        TaskList.objects.create(task_user=self.test_prof, task_list_name="test_item_edit_due_date")
        test_list = TaskList.objects.get(task_list_name="test_item_edit_due_date")
        TaskItem.objects.create(task_name="test_item_edit_due_date", task_list=test_list)
        test_item = TaskItem.objects.get(task_name="test_item_edit_due_date")
        new_time = datetime.now() + timedelta(days=1)
        test_item.edit_due_date(new_time)
        self.assertEqual(test_item.task_due_date, new_time)

    def test_item_edit_priority(self):
        TaskList.objects.create(task_user=self.test_prof, task_list_name="test_item_edit_priority")
        test_list = TaskList.objects.get(task_list_name="test_item_edit_priority")
        TaskItem.objects.create(task_name="test_item_edit_priority", task_list=test_list)
        test_item = TaskItem.objects.get(task_name="test_item_edit_priority")
        self.assertEqual(test_item.task_priority, 1)
        test_item.edit_priority(2)
        self.assertEqual(test_item.task_priority, 2)

    def test_item_complete_toggle(self):
        TaskList.objects.create(task_user=self.test_prof, task_list_name="test_item_complete_toggle")
        test_list = TaskList.objects.get(task_list_name="test_item_complete_toggle")
        TaskItem.objects.create(task_name="test_item_complete_toggle", task_list=test_list)
        test_item = TaskItem.objects.get(task_name="test_item_complete_toggle")
        before_item_completion = test_item.task_completion
        test_item.complete_toggle()
        self.assertEqual(test_item.task_completion, not before_item_completion)

    def test_item___str__(self):
        TaskList.objects.create(task_user=self.test_prof, task_list_name="test_item___str__")
        test_list = TaskList.objects.get(task_list_name="test_item___str__")
        TaskItem.objects.create(task_name="test_item___str__", task_list=test_list)
        test_item = TaskItem.objects.get(task_name="test_item___str__")
        self.assertEqual(test_item.task_name, test_item.__str__())

class grade_calc_urls_test(TestCase):
    def setUp(self):
        client = Client()
        user = get_user_model()
        self.test_user = user.objects.get_or_create(username="test_user", password="password")[0]
        self.client.force_login(self.test_user)

    def test_grade_calc(self):
        response = self.client.get('/dashboard/grade_calc/')
        self.assertEqual(response.status_code, 200)
        
class grade_calc_view_test(TestCase):
    def setUp(self):
        self.client = Client()
        user = get_user_model()
        self.test_user = user.objects.get_or_create(username="test_user", password="password")[0]
        self.client.force_login(self.test_user)

    def test_get_grade_calc_results_authenticated_valid_weight_total(self):
        response = self.client.post(
            '/dashboard/grade_calc/',
            data={
                'form-TOTAL_FORMS': 2,
                'form-INITIAL_FORMS': 0,
                'form-0-category_weight': 30,
                'form-0-current_points_earned': 30,
                'form-0-current_points_possible': 50,
                'form-0-total_points_possible': 100,
                'form-1-category_weight': 70,
                'form-1-current_points_earned': 30,
                'form-1-current_points_possible': 50,
                'form-1-total_points_possible': 100,
            },
        )
        self.assertTemplateUsed(response, 'grade_calc_results.html')

    def test_get_grade_calc_results_authenticated_invalid_weight_total_1(self):
        response = self.client.post(
            '/dashboard/grade_calc/',
            data={
                'form-TOTAL_FORMS': 2,
                'form-INITIAL_FORMS': 0,
                'form-0-category_weight': 50,
                'form-0-current_points_earned': 30,
                'form-0-current_points_possible': 50,
                'form-0-total_points_possible': 100,
                'form-1-category_weight': 49,
                'form-1-current_points_earned': 30,
                'form-1-current_points_possible': 50,
                'form-1-total_points_possible': 100,
            },
        )
        self.assertTemplateNotUsed(response, 'grade_calc_results.html')

    def test_get_grade_calc_results_authenticated_invalid_weight_total_2(self):
        response = self.client.post(
            '/dashboard/grade_calc/',
            data={
                'form-TOTAL_FORMS': 2,
                'form-INITIAL_FORMS': 0,
                'form-0-category_weight': 50,
                'form-0-current_points_earned': 30,
                'form-0-current_points_possible': 50,
                'form-0-total_points_possible': 100,
                'form-1-category_weight': 51,
                'form-1-current_points_earned': 30,
                'form-1-current_points_possible': 50,
                'form-1-total_points_possible': 100,
            },
        )
        self.assertTemplateNotUsed(response, 'grade_calc_results.html')

    def test_get_grade_calc_results_authenticated_all_points_given(self):
        response = self.client.post(
            '/dashboard/grade_calc/',
            data={
                'form-TOTAL_FORMS': 2,
                'form-INITIAL_FORMS': 0,
                'form-0-category_weight': 50,
                'form-0-current_points_earned': 30,
                'form-0-current_points_possible': 100,
                'form-0-total_points_possible': 100,
                'form-1-category_weight': 50,
                'form-1-current_points_earned': 30,
                'form-1-current_points_possible': 100,
                'form-1-total_points_possible': 100,
            },
        )
        self.assertFalse(response.context['show_grade_table'])
    
    def test_get_grade_calc_results_authenticated_invalid_total_points_possible(self):
        response = self.client.post(
            '/dashboard/grade_calc/',
            data={
                'form-TOTAL_FORMS': 2,
                'form-INITIAL_FORMS': 0,
                'form-0-category_weight': 30,
                'form-0-current_points_earned': 0,
                'form-0-current_points_possible': 0,
                'form-0-total_points_possible': 0,
                'form-1-category_weight': 70,
                'form-1-current_points_earned': 30,
                'form-1-current_points_possible': 50,
                'form-1-total_points_possible': 100,
            },
        )
        self.assertTemplateNotUsed(response, 'grade_calc_results.html')

    def test_get_grade_calc_results_authenticated_invalid_current_points_possible(self):
        response = self.client.post(
            '/dashboard/grade_calc/',
            data={
                'form-TOTAL_FORMS': 2,
                'form-INITIAL_FORMS': 0,
                'form-0-category_weight': 30,
                'form-0-current_points_earned': 0,
                'form-0-current_points_possible': -1,
                'form-0-total_points_possible': 10,
                'form-1-category_weight': 70,
                'form-1-current_points_earned': 30,
                'form-1-current_points_possible': 50,
                'form-1-total_points_possible': 100,
            },
        )
        self.assertTemplateNotUsed(response, 'grade_calc_results.html')

    def test_get_grade_calc_results_authenticated_invalid_current_earned_points(self):
        response = self.client.post(
            '/dashboard/grade_calc/',
            data={
                'form-TOTAL_FORMS': 2,
                'form-INITIAL_FORMS': 0,
                'form-0-category_weight': 30,
                'form-0-current_points_earned': -1,
                'form-0-current_points_possible': 5,
                'form-0-total_points_possible': 10,
                'form-1-category_weight': 70,
                'form-1-current_points_earned': 30,
                'form-1-current_points_possible': 50,
                'form-1-total_points_possible': 100,
            },
        )
        self.assertTemplateNotUsed(response, 'grade_calc_results.html')

class grade_calc_form_test(TestCase):
    def setUp(self):
        self.client = Client()
        user = get_user_model()
        self.test_user = user.objects.get_or_create(username="test_user", password="password")[0]
        self.client.force_login(self.test_user)

    def form_data(self, weight, earned, possible, total):
        return GradeCategoryForm(
            data={
                'category_weight': weight,
                'current_points_earned': earned,
                'current_points_possible': possible,
                'total_points_possible': total,
            }
        )

    def test_valid_grade_category_form(self):
        form = self.form_data(20, 30, 50, 100)
        self.assertTrue(form.is_valid())

    def test_grade_category_form_missing_weight(self):
        form = self.form_data("", 30, 50, 100)
        self.assertFalse(form.is_valid())

    def test_grade_category_form_missing_earned(self):
        form = self.form_data(20, "", 50, 100)
        self.assertFalse(form.is_valid())

    def test_grade_category_form_missing_possible(self):
        form = self.form_data(20, 30, "", 100)
        self.assertFalse(form.is_valid())

    def test_grade_category_form_missing_total(self):
        form = self.form_data(20, 30, 50, "")
        self.assertFalse(form.is_valid())

class weather_test(TestCase):
    def setUp(self):
        client = Client()
        user = get_user_model()
        self.test_user = user.objects.get_or_create(username="test_user", password="password")[0]
        self.client.force_login(self.test_user)
        self.test_prof = Profile.objects.get(user=self.test_user)

    def test_create_city(self):
        before_num_cities = City.objects.count()
        City.objects.create(city_user=self.test_prof, name="test_create_city")
        test_city = City.objects.get(name="test_create_city")
        self.assertEqual(before_num_cities+1, City.objects.count())

    def test_delete_city(self):
        before_num_cities = City.objects.count()
        City.objects.create(city_user=self.test_prof, name="test_delete_city")
        test_city = City.objects.get(name="test_delete_city")
        test_city.delete()
        self.assertEqual(before_num_cities, City.objects.count())
        self.assertRaises(City.DoesNotExist, City.objects.get, name="test_delete_city")

    def test_city___str__(self):
        City.objects.create(city_user=self.test_prof, name="test_city___str__")
        test_city = City.objects.get(name="test_city___str__")
        self.assertEqual(test_city.name, test_city.__str__())