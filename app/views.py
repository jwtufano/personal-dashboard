from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound
from decimal import *
from django.forms.formsets import formset_factory
import requests
import calendar

from app.forms import TaskItemForm, TaskListForm, GradeCategoryForm
from weather.models import City
from weather.forms import CityForm

from datetime import datetime, timedelta, date
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe
from models.models import *
from .utils import Calendar

# Create your views here.
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def make_calendar(request):
    if request.user.is_authenticated:
        d = get_date(request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        cal.setfirstweekday(6)
        html_cal = cal.formatmonth(withyear=True)
        context = {'calendar' : html_cal, 'prev_month' : prev_month(d), 'next_month' : next_month(d)}
        return render(request, 'calendar.html', context)
    return HttpResponseRedirect(reverse('home'))

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
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f0ec1cf58c705f937e3cd62b5a0e5f14'
        cities = City.objects.all() #return all the cities in the database
    
        if request.method == 'POST': # only true if form is submitted
            form = CityForm(request.POST) # add actual request data to form for processing
            form.save() # will validate and save if validate
    
        form = CityForm()

        weather_data = []
        for city in cities:

            city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

            weather = {
                'city' : city,
                'temperature' : city_weather['main']['temp'],
                'description' : city_weather['weather'][0]['description'],
                'icon' : city_weather['weather'][0]['icon']
            }

            weather_data.append(weather) #add the data for the current city into our list

        context = {'weather_data' : weather_data, 'form' : form}
        return render(request, 'dashboard.html', context) #returns the index.html template
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
            percentage_total_points_given = Decimal(0)
            total_weight = Decimal(0)
            for form in formset:
                if form.is_valid():
                    grade += form.cleaned_data['category_weight']*Decimal(form.cleaned_data['current_points_earned']/Decimal(form.cleaned_data['current_points_possible']))
                    percentage_total_points_given += form.cleaned_data['category_weight']*Decimal(form.cleaned_data['current_points_earned']/Decimal(form.cleaned_data['total_points_possible']))
                    total_weight += form.cleaned_data['category_weight']
            grade = round(grade, 2)
            show_grade_table = not (percentage_total_points_given < 100.1 and percentage_total_points_given > 99.9)
            if show_grade_table:
                grade_for_98 = round(max((9800-(grade*percentage_total_points_given))/(100-percentage_total_points_given), 0), 2)
                grade_for_93 = round(max((9300-(grade*percentage_total_points_given))/(100-percentage_total_points_given), 0), 2)
                grade_for_90 = round(max((9000-(grade*percentage_total_points_given))/(100-percentage_total_points_given), 0), 2)
                grade_for_88 = round(max((8800-(grade*percentage_total_points_given))/(100-percentage_total_points_given), 0), 2)
                grade_for_83 = round(max((8300-(grade*percentage_total_points_given))/(100-percentage_total_points_given), 0), 2)
                grade_for_80 = round(max((8000-(grade*percentage_total_points_given))/(100-percentage_total_points_given), 0), 2)
                grade_for_78 = round(max((7800-(grade*percentage_total_points_given))/(100-percentage_total_points_given), 0), 2)
                grade_for_73 = round(max((7300-(grade*percentage_total_points_given))/(100-percentage_total_points_given), 0), 2)
                grade_for_70 = round(max((7000-(grade*percentage_total_points_given))/(100-percentage_total_points_given), 0), 2)
                grade_for_68 = round(max((6800-(grade*percentage_total_points_given))/(100-percentage_total_points_given), 0), 2)
                grade_for_63 = round(max((6300-(grade*percentage_total_points_given))/(100-percentage_total_points_given), 0), 2)
                grade_for_60 = round(max((6000-(grade*percentage_total_points_given))/(100-percentage_total_points_given), 0), 2)
            else:
                grade_for_98 = round(0, 2)
                grade_for_93 = round(0, 2)
                grade_for_90 = round(0, 2)
                grade_for_88 = round(0, 2)
                grade_for_83 = round(0, 2)
                grade_for_80 = round(0, 2)
                grade_for_78 = round(0, 2)
                grade_for_73 = round(0, 2)
                grade_for_70 = round(0, 2)
                grade_for_68 = round(0, 2)
                grade_for_63 = round(0, 2)
                grade_for_60 = round(0, 2)

            if total_weight < 100.1 and total_weight > 99.9:
                context = {
                    'grade': grade,
                    'grade_for_98': grade_for_98,
                    'grade_for_93': grade_for_93,
                    'grade_for_90': grade_for_90,
                    'grade_for_88': grade_for_88,
                    'grade_for_83': grade_for_83,
                    'grade_for_80': grade_for_80,
                    'grade_for_78': grade_for_78,
                    'grade_for_73': grade_for_73,
                    'grade_for_70': grade_for_70,
                    'grade_for_68': grade_for_68,
                    'grade_for_63': grade_for_63,
                    'grade_for_60': grade_for_60,
                    'show_grade_table': show_grade_table,
                }

                return render(request, 'grade_calc_results.html', context)
            else:
                context = {
                    'formset': formset,
                    'total_weight': total_weight,
                }

                return render(request, 'grade_calc.html', context)

    context = {
        'formset': formset,
    }

    return render(request, 'grade_calc.html', context)

def grade_calc_results(request):
    pass
