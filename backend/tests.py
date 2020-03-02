from django.test import TestCase
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