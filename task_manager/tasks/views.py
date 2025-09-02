from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from task_manager.mixins import OwnTaskMixin
from task_manager.tasks.forms import TaskFilterForm, TaskForm
from task_manager.tasks.models import Task


class TaskIndexView(ListView):
    queryset = Task.objects.all().order_by("id")
    template_name = "tasks/index.html"
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = super().get_queryset()
        status_id = self.request.GET.get("status")
        if status_id:
            queryset = queryset.filter(status__id=status_id)
        executor_id = self.request.GET.get("executor")
        if executor_id:
            queryset = queryset.filter(executor__id=executor_id)
        self_tasks = self.request.GET.get("self_tasks")
        if self_tasks == "on":
            user_id = self.request.user.id
            queryset = queryset.filter(author__id=user_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            filter_form = TaskFilterForm(self.request.GET)
        else:
            filter_form = TaskFilterForm()
        context["filter_form"] = filter_form
        return context


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_message = _("Task has been successfully created")
    template_name = "tasks/create.html"
    success_url = reverse_lazy("tasks_index")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(
    SuccessMessageMixin,
    UpdateView,
):
    model = Task
    form_class = TaskForm
    success_message = _("Task has been successfully updated")
    template_name = "tasks/update.html"
    success_url = reverse_lazy("tasks_index")


class TaskDeleteView(
    OwnTaskMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Task
    success_message = _("Task has been successfully deleted")
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks_index")


class TaskDetailView(
    DetailView,
):
    template_name = "tasks/detail.html"
    model = Task
