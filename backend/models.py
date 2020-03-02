import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser):
    pass


class Task(models.Model):
	task_name = models.CharField(max_length = 100)
	due_date = models.DateTimeField('date due')
	task_description = models.CharField(max_length = 500)
	subtasks = {}

	def __str__(self):
		return self.task_name + ":" + self.task_description


class TaskList(models.Model):
	Tasks = {}
	tasklist_name = models.CharField(max_length = 100)
	tasklist_description = models.CharField(max_length = 500)
	#Considering using https://github.com/fabiocaccamo/django-colorfield for color
	tasklist_color = '#0000FF'

	def __str__(self):
		return self.list_name
	#Add a task into the tasklist
	def addTask(self, task):
		self.Tasks[task.task_name] = task
		return self.Tasks

	#Delete a task from the tasklist
	def delTask(self, name):
		del self.Tasks[name]
		return self.Tasks

class TaskListGroup(models.Model):
	TaskLists = {}
	tasklist_group_name = models.CharField(max_length = 100)
	#Considering using https://github.com/fabiocaccamo/django-colorfield for color
	tasklist_group_color = models.CharField(max_length = 7)

class Event(models.Model):
	date_time = models.DateTimeField('Event date')
	event_name = models.CharField(max_length = 100)
	event_description = models.CharField(max_length = 500)
	event_color = '#0000FF'

class EventList(models.Model):
	events = {}
	eventlist_name = models.CharField(max_length = 100)
	eventlist_description = models.CharField(max_length = 500)

class Course(models.Model):
	course_name = models.CharField(max_length = 100)
	grade_categories = {}

class GradeCategory(models.Model):
	parent_course_name = models.CharField(max_length = 100)
	category_name = models.CharField(max_length = 100)
	weight = models.DecimalField
	grades = {}

class Grade(models.Model):
	parent_course_name = models.CharField(max_length = 100)
	parent_category_name = models.CharField(max_length = 100)
	earned_points = models.IntegerField()
	possible_points = models.IntegerField()