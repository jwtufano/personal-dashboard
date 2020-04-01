from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .forms import CustomUserCreationForm, TaskListCreationForm, TaskCreationForm, TaskCompletionForm
from .models import Task, TaskList

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class TodoView(TemplateView):
    template_name = 'backend/todo.html'
    form_class = TaskCompletionForm

class TaskListView(DetailView):
    template_name = 'backend/tasklist_detail.html'

    def get_queryset(self):
        return TaskList.objects.all()

class TaskView(DetailView):
    template_name = 'backend/task_detail.html'

    def get_queryset(self):
        return Task.objects.all()

class CreateTaskListView(CreateView):
    form_class = TaskListCreationForm
    success_url = reverse_lazy('todo')
    template_name = 'backend/create-list.html'

    def form_valid(self, form):
        task_list = form.save(commit=False)
        task_list.user = self.request.user
        task_list.save()
        return redirect(self.success_url)

class CreateTaskView(CreateView):
    form_class = TaskCreationForm
    template_name = 'backend/create-task.html'

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        pk = self.kwargs.get(self.pk_url_kwarg)
        task.task_list = self.request.user.tasklist_set.all().filter(pk=pk).get()
        task.save()
        return redirect('/backend/todo/list/' + str(pk))

class CreateSubtaskView(CreateView):
    form_class = TaskCreationForm
    template_name = 'backend/create-task.html'

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        pk = self.kwargs.get(self.pk_url_kwarg)
        task.parent_task = Task.objects.all().filter(pk=pk).get()
        task.task_list = task.parent_task.task_list
        task.save()
        return redirect('/backend/todo/task/' + str(pk))

class EditTaskView(UpdateView):
    form_class = TaskCreationForm
    template_name = 'backend/create-task.html'

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        pk = self.kwargs.get(self.pk_url_kwarg)
        task.task_list = self.request.user.tasklist_set.all().filter(pk=pk).get()
        task.save()
        return redirect('/backend/todo/list/' + str(pk))

class EditListView(UpdateView):
    form_class = TaskListCreationForm
    success_url = reverse_lazy('todo')
    template_name = 'backend/create-list.html'

    def form_valid(self, form):
        task_list = form.save(commit=False)
        task_list.user = self.request.user
        task_list.save()
        return redirect(self.success_url)