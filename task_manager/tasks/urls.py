from django.urls import path

from task_manager.tasks.views import (
    TaskCreateView,
    TaskDeleteView,
    TaskDetailView,
    TaskIndexView,
    TaskUpdateView,
)

urlpatterns = [
    path("", TaskIndexView.as_view(), name="tasks_index"),
    path("create/", TaskCreateView.as_view(), name="tasks_create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="tasks_update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="tasks_delete"),
    path("<int:pk>/", TaskDetailView.as_view(), name="tasks_detail"),
]
