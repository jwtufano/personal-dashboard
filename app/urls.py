from django.contrib import admin
from django.urls import include, path

from . import views

app_name = "dashboard"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create_list/", views.create_list, name="create_list"),
    path("create_item/", views.create_item, name="create_item"),
    path("update_list/", views.update_list, name="update_list"),
    path("update_item/", views.update_item, name="update_item"),
    path("todo/", views.todo, name="todo"),
    path("grade_calc/", views.grade_calc, name="grade_calc"),
    path("grade_calc/results/", views.grade_calc_results, name="grade_calc_results"),
]
