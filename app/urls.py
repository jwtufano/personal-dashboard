from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from . import views

app_name = "dashboard"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create_list/", views.create_list, name="create_list"),
    path("create_item/", views.create_item, name="create_item"),
    path("update_list/", views.update_list, name="update_list"),
    path("edit_item/<int:task_id>/", views.update_item, name="edit_item"),
    path("todo/", views.todo, name="todo"),
    path("view_items/", views.list_items, name="view_items"),
    path("view_completed_items/", views.list_completed_items, name="view_completed_items"),
    path("view_lists/", views.list_lists, name="view_lists"),
    path("grade_calc/", views.grade_calc, name="grade_calc"),
    path("grade_calc/results/", views.grade_calc_results, name="grade_calc_results"),
    path("calendar/", views.make_calendar, name="calendar"),
    path("complete/<int:task_id>/", views.complete, name="complete"),
    path("uncomplete/<int:task_id>/", views.uncomplete, name="uncomplete"),
    path("delete_item/<int:task_id>/", views.delete_item, name="delete_item"),
    path("delete_completed_item/<int:task_id>/", views.delete_completed_item, name="delete_completed_item"),
    path("delete_list/", views.delete_list, name="delete_list"),
    path("delete_city/<int:city_id>/", views.delete_city, name="delete_city"),
]
