from decimal import *

from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory

from models.models import TaskItem, TaskList
from app.forms import TaskItemForm, TaskListForm, GradeCategoryForm

# Create your views here.
def create_list(request):
    # add form template
    if request.method == 'POST':
        form = TaskListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("dashboard:dashboard"))
    else:
        form = TaskListForm()
    return render(request, 'create_list_form.html', {"form": form})

def update_list(request):
    # add form template
    if request.method == 'POST':
        form = TaskListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("dashboard:dashboard"))
    else:
        form = TaskListForm()
    return render(request, 'create_list_form.html', {"form": form})

def delete_list(request):
    # if post request, remove the list using TaskList.objects.get()
    pass

def list_lists(request):
    # return list that is TaskLists.objects.get()
    pass

def create_item(request):
    # add form template
    if request.method == 'POST':
        form = TaskItemForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse("dashboard:dashboard"))
    else:
        form = TaskItemForm()
    return render(request, 'create_item_form.html', {"form": form})

def update_item(request):
    # add form template
    if request.method == 'POST':
        form = TaskItemForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse("dashboard:dashboard"))
    else:
        form = TaskItemForm()
    return render(request, 'create_item_form.html', {"form": form})

def delete_list(request):
    # if post request, remove the list using TaskList.objects.get()
    pass

def list_items(request):
    # second parameter for TaskList and return list that is TaskItems.objects.get(TaskList=passed_list)
    pass


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')
    return HttpResponseRedirect(reverse('home'))

def todo(request):
    if request.user.is_authenticated:
        return render(request, 'todo.html')
    return HttpResponseRedirect(reverse('home'))

def grade_calc(request):
    GradeCalcFormSet = formset_factory(GradeCategoryForm)
    formset = GradeCalcFormSet()

    if request.method == "POST":
        formset = GradeCalcFormSet(request.POST)
        if formset.is_valid():
            grade = Decimal(0)
            for form in formset:
                grade += form.cleaned_data['category_weight']*Decimal(form.cleaned_data['current_points_earned']/form.cleaned_data['current_points_possible'])
            grade = round(grade, 2)

            context = {
                'grade': grade,
            }

            return render(request, 'grade_calc_results.html', context)

    context = {
        'formset': formset,
    }

    return render(request, 'grade_calc.html', context)

def grade_calc_results(request):
    pass