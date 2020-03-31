from django.test import TestCase
from django.contrib.auth import get_user_model
from backend.models import Task, TaskList, TaskListGroup, Event, EventList, \
                           Course, GradeCategory, Grade

class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create()
        Task.objects.create(task_name="Test Name", task_description="Test description")

    def test_default_task_name_setup(self):
        default = Task.objects.get(id=1)
        self.assertEqual(default.task_name, "Task")
    
    def test_default_task_description_setup(self):
        default = Task.objects.get(id=1)
        self.assertEqual(default.task_description, "Task description")
    
    def test_default_task_str(self):
        default = Task.objects.get(id=1)
        self.assertEqual(default.__str__(), "Task: Task description")

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
