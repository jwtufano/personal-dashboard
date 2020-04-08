from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from decimal import *
from django.forms.formsets import formset_factory

from models.models import TaskItem, TaskList
from app.forms import TaskItemForm, TaskListForm, GradeCategoryForm

# Create your views here.
def create_list(request):
    if request.method == "POST":
        form = TaskListForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("dashboard:dashboard"))
    else:
        form = TaskListForm()
    return render(request, "create_list_form.html", {"form": form})


def update_list(request):
    if request.method == "POST":
        data = TaskList.objects.get_object_or_404(task_list_name=request.POST.get("task_list_name"))
        form = TaskListForm(request.POST, initial=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("dashboard:dashboard"))
    else:
        form = TaskListForm()
    return render(request, "create_list_form.html", {"form": form})


def delete_list(request):
    if request.method == "POST":
        if 'delete' in request.POST:
            item = TaskList.objects.get_object_or_404(task_list_name=request.POST.get("task_list_name"))
            if item:
                item.delete()
                return HttpResponseRedirect(reverse("dashboard:dashboard"))
    return HttpResponseRedirect(reverse("dashboard:dashboard"))


def list_lists(request):
    try:
        task_list = list(TaskList.objects.all())
    except TaskList.DoesNotExist:
        return HttpResponseRedirect(reverse("dashboard:dashboard"))
    return render(request, "list-lists.html", {"task_list": task_list})


def create_item(request):
    if request.method == "POST":
        form = TaskItemForm(request.POST)
        if form.is_valid():
            item = TaskItem()
            item.task_name = form.cleaned_data['task_name']
            item.task_description = form.cleaned_data['task_description']
            item.task_created_date = form.cleaned_data['task_created_date']
            item.task_due_date = form.cleaned_data['task_due_date']
            item.task_priority = form.cleaned_data['task_priority']
            item.task_completion = form.cleaned_data['task_completion']
            item.task_list = form.cleaned_data['task_list']
            item.save()
            return HttpResponseRedirect(reverse("dashboard:dashboard"))
    else:
        form = TaskItemForm()
    return render(request, "create_item_form.html", {"form": form})


def update_item(request):
    if request.method == "POST":
        data = TaskItem.objects.get_object_or_404(task_list_name=request.POST.get("task_name"))
        form = TaskItemForm(request.POST, initial=data)
        if form.is_valid():
            item = TaskItem()
            item.task_name = form.cleaned_data['task_name']
            item.task_description = form.cleaned_data['task_description']
            item.task_created_date = form.cleaned_data['task_created_date']
            item.task_due_date = form.cleaned_data['task_due_date']
            item.task_priority = form.cleaned_data['task_priority']
            item.task_completion = form.cleaned_data['task_completion']
            item.task_list = form.cleaned_data['task_list']
            item.save()
            return HttpResponseRedirect(reverse("dashboard:dashboard"))
    else:
        form = TaskItemForm()
    return render(request, "create_item_form.html", {"form": form})


def delete_item(request):
    if request.method == "POST":
        if 'delete' in request.POST:
            item = TaskItem.objects.get_object_or_404(task_list_name=request.POST.get("task_name"))
            if item:
                item.delete()
                return HttpResponseRedirect(reverse("dashboard:dashboard"))
    return HttpResponseRedirect(reverse("dashboard:dashboard"))


def list_items(request):
    # second parameter for TaskList and return list that is TaskItems.objects.get(TaskList=passed_list)
    try:
        items = TaskItem.objects.all()
    except TaskList.DoesNotExist:
        return HttpResponseRedirect(reverse("dashboard:dashboard"))
    task_lists = []
    for item in items:
        if item.task_list not in task_lists:
            task_lists.append(item.task_list)
    lists = []
    for task_list in task_lists:
        helper = []
        helper.append(task_list)
        why = list(TaskItem.objects.filter(task_list=task_list))
        for item in why:
            helper.append(item)
        lists.append(helper)
    print(lists)
    return render(request, "list-items.html", {"items": items, "lists": lists, "task_lists": task_lists})


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
