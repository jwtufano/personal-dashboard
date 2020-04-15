from django.forms.formsets import BaseFormSet
from django.forms import ModelForm, ChoiceField
from django import forms
from models.models import TaskItem, TaskList, CHOICES

class TaskListForm(ModelForm):
    class Meta:
        model = TaskList
        fields = ['task_list_name', 'task_list_description']

class TaskItemForm(forms.Form):
    task_name = forms.CharField(max_length=100, required=True)
    task_description = forms.CharField(max_length=100, required=True)
    task_created_date = forms.DateTimeField(
        required = True,
        error_messages={
            "required": "Please enter a valid date.",
            "invalid": "Please enter a valid Created date",
        })
    task_due_date = forms.DateTimeField(
        required = True,
        error_messages={
            "required": "Please enter a valid date.",
            "invalid": "Please enter a valid Due date",
        })
    task_priority = forms.ChoiceField(choices=CHOICES)
    task_completion = forms.BooleanField()
    task_list = forms.ModelChoiceField(queryset=TaskList.objects.all(), error_messages = {"required": "Please choose a List"})

class GradeCategoryForm(forms.Form):
    category_weight = forms.DecimalField(max_value=100, min_value=0, decimal_places=2, required=True)
    current_points_earned = forms.IntegerField(min_value=0, required=True)
    current_points_possible = forms.IntegerField(min_value=0, required=True)
    total_points_possible = forms.IntegerField(min_value=0, required=True)

class BaseGradeCategoryFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        
        weights = []
        urls = []
        
        for form in self.forms:
            if form.cleaned_data:
                current_points_earned = form.cleaned_data['current_points_earned']
                current_points_possible = form.cleaned_data['current_points_possible']
                total_points_possible = form.cleaned_data['total_points_possible']