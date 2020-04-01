from django.urls import path

from .views import HomePageView, SignUpView, TodoView, TaskListView, TaskView, CreateTaskListView, CreateTaskView, CreateSubtaskView, EditListView, EditTaskView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('todo/', TodoView.as_view(), name='todo'),
    path('todo/list/<int:pk>', TaskListView.as_view(), name='tasklist'),
    path('todo/task/<int:pk>', TaskView.as_view(), name='task'),
    path('todo/create-list', CreateTaskListView.as_view(), name='create-list'),
    path('todo/<int:pk>/create-task', CreateTaskView.as_view(), name='create-task'),
    path('todo/<int:pk>/create-subtask', CreateSubtaskView.as_view(), name='create-subtask'),
    path('todo/<int:pk>/edit-list', EditListView.as_view(), name='edit-list'),
    path('todo/<int:pk>/edit-task', EditTaskView.as_view(), name='edit-task'),
]