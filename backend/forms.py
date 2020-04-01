from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Task, TaskList

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

class TaskListCreationForm(forms.ModelForm):

    class Meta:
        model = TaskList
        fields = ['tasklist_name', 'tasklist_description']

class TaskCreationForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['task_name', 'task_description', 'task_due_date', 'task_completion']

class TaskCompletionForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['task_completion']