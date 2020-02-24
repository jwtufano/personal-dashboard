import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser):
    pass


class Task(models.Model):
	task_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date due')
	task_description = models.CharField(max_length=500)

	def __str__(self):
		return self.task_name + ":" + self.task_description


class TaskList(models.Model):
	Tasks = {}
	list_name = models.CharField(max_length =200)

	def __str__(self):
		return self.list_name
	#Add a task into the tasklist
	def addTask(self, task):
		self.Tasks[task.task_name] = task
		return self.Tasks

	#Delete a task from the tasklist
	def delTask(self, name):
		del self.Tasks.name
		return self.Tasks
