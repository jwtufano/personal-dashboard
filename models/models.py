from django.db import models

from datetime import date, datetime, timedelta

from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
CHOICES = [(1, 'low'), (2, 'normal'), (3, 'high')]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city_list = ArrayField(models.CharField(max_length=20, blank=True))

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, city_list=[""])

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class TaskList(models.Model):
    task_user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    task_list_name = models.CharField(max_length=100, default="To Do List") # , unique=True)
    task_list_description = models.CharField(max_length = 100, default="My To Do List")

    def add_task(self, task):
        self.tasks.add(task)
        return self.task

    def remove_task(self, task):
        self.tasks.remove(task)
        return self.task

    def __str__(self):
        return self.task_list_name

    class Meta:
        ordering = ['task_list_name']


class TaskItem(models.Model):
    task_name=models.CharField(max_length=100, default='Task')
    tast_description=models.CharField(max_length = 100, default='Task Description')
    task_created_date = models.DateTimeField(default=datetime.now())
    task_due_date=models.DateTimeField(default=datetime.now())
    task_priority=models.IntegerField(choices=CHOICES, default=1)
    task_completion= models.BooleanField(default=False)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE, default=None, blank=True, null=False)

    def edit_name(self, new_name):
        self.task_name = new_name

    def edit_description(self, new_description):
        self.task_description = new_description

    def edit_due_date(self, new_due_date):
        self.task_due_date = new_due_date

    # TODO add check for good value
    def edit_priority(self, new_priority):
        self.task_priority = new_priority

    def complete_toggle(self):
        self.task_completion = not self.task_completion

    def edit_list(self, new_task_list):
        if (self.task_list is not None):
            self.task_list.remove_task(self)
        new_task_list.add_task(self)

    def __str__(self):
        return self.task_name

    class Meta:
        ordering = ['task_due_date']

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actual city name on the dashboard
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'
