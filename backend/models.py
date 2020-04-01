import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class CustomUser(AbstractUser):
    pass

def tomorrow():
	return timezone.now() + timezone.timedelta(days=1)

class Task(models.Model):
	DEFAULT_PK = 1
	task_name = models.CharField(max_length = 100, default='Task')
	task_description = models.CharField(max_length = 500, default='Task description')
	task_due_date = models.DateTimeField(default=tomorrow)
	task_completion = models.BooleanField(default=False)
	parent_task = models.ForeignKey('backend.Task', on_delete=models.CASCADE, default=None, blank=True, null=True)
	task_list = models.ForeignKey('backend.TaskList', on_delete=models.CASCADE, default=None, blank=True, null=True)

	def edit_name(self, input_name):
		self.task_name = input_name
		
	def edit_desc(self, input_desc):
		self.task_desc = input_desc
		
	def edit_due_date(self, input_due_date):
		self.task_due_date = input_due_date
		
	def change_completion(self):
		self.task_completion = not self.task_completion

	def remove_from_parent_task(self):
		if (self.parent_task is not None):
			parent_parent = self.parent_task.parent_task
			if (parent_parent is not None):
				parent_parent.task_set.add(self)
			else:
				self.parent_task.task_set.remove(self)
			
	
	def edit_list(self, input_list):
		if (self.parent_task is not None):
			self.parent_task.task_set.remove(self)
		input_list.task_set.add(self)
	
	def __str__(self):
		return self.task_name

class TaskList(models.Model):
	tasklist_name = models.CharField(max_length = 100, default='Task List')
	tasklist_description = models.CharField(max_length = 500, default='A list of tasks.')
	user = models.ForeignKey('backend.CustomUser', on_delete=models.CASCADE, default=None, blank=True, null=True)

	#Considering using https://github.com/fabiocaccamo/django-colorfield for color
	#tasklist_color = '#0000FF'

	def __str__(self):
		return self.tasklist_name
	
	#Add a task into the tasklist
	def add_task(self, task):
		self.tasks.add(task)
		return self.tasks

	#Remove a task from the tasklist
	def remove_task(self, task):
		self.tasks.remove(task)
		return self.tasks

# class TaskListGroup(models.Model):
# 	tasklist_group_name = models.CharField(max_length = 100, default='TaskList Group')
# 	TaskLists = {}
# 	#Considering using https://github.com/fabiocaccamo/django-colorfield for color
# 	#tasklist_group_color = models.CharField(max_length = 7)

# 	def __str__(self):
# 		return self.tasklist_group_name

# class Event(models.Model):
# 	event_name = models.CharField(max_length = 100, default='Event')
# 	event_description = models.CharField(max_length = 500, default='Event description')
# 	date_time = models.DateTimeField('event date and time', default=timezone.now)
# 	#event_color = '#0000FF'

# 	def __str__(self):
# 		return self.event_name + ': ' + self.date_time

# class EventList(models.Model):
# 	eventlist_name = models.CharField(max_length = 100)
# 	eventlist_description = models.CharField(max_length = 500)
# 	events = {}

# 	def __str__(self):
# 		return self.eventlist_name + ': ' + self.eventlist_description

# class Course(models.Model):
# 	course_name = models.CharField(max_length = 100)
# 	grade_categories = {}

# 	def __str__(self):
# 		return self.course_name

# class GradeCategory(models.Model):
# 	parent_course = models.ForeignKey(Course, on_delete=models.CASCADE)
# 	category_name = models.CharField(max_length = 100)
# 	weight = models.DecimalField
# 	grades = {}

# 	def __str__(self):
# 		return self.category_name + ': ' + weight + '\%'

# class Grade(models.Model):
# 	parent_category = models.ForeignKey(GradeCategory, on_delete=models.CASCADE)
# 	grade_name = models.CharField(max_length = 100, default='Grade')
# 	earned_points = models.IntegerField()
# 	possible_points = models.IntegerField()

# 	def __str__(self):
# 		return parent_category.category_name + ' - ' + self.grade_name + ': ' \
# 			   + self.earned_points + '/' + self.possible_points