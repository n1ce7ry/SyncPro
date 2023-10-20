from django.urls import path
from django.contrib.auth.decorators import login_required

from tasks import views

urlpatterns = [
    path('', views.TasksListView.as_view(), name='tasks'),
    path('add-task/', login_required(views.AddTaskView.as_view()), name='add_task'),
    path('delete/<int:pk>/', login_required(views.DeleteTaskView.as_view()), name='delete_task'),
    path('<int:pk>/', login_required(views.EditTaskView.as_view()), name='edit_task'),
    path(
         'filter/',
         login_required(views.FilterTasksListView.as_view()),
         name='filter_tasks'
    ),
]
