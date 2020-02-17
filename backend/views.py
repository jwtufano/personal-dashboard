from django.shortcuts import render
from django.views import generic

from .models import Task, TaskList

class TaskListView(generic.ListView):
  template_name = 'backend/tasklist.html'
  context_object_name = 'tasklist'

  def get_queryset(self):
    return TaskList.objects