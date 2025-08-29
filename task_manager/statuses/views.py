from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import LoginRequiredWithMessageMixin
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status


class StatusIndexView(LoginRequiredWithMessageMixin, ListView):
    queryset = Status.objects.all().order_by("id")
    template_name = "statuses/index.html"
    context_object_name = "statuses"


class StatusCreateView(
    LoginRequiredWithMessageMixin, SuccessMessageMixin, CreateView
):
    model = Status
    form_class = StatusForm
    success_message = _("Status has been successfully registered")
    template_name = "statuses/create.html"
    success_url = reverse_lazy("statuses_index")


class StatusUpdateView(
    LoginRequiredWithMessageMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = Status
    form_class = StatusForm
    success_message = _("Status has been successfully updated")
    template_name = "statuses/update.html"
    success_url = reverse_lazy("statuses_index")


class StatusDeleteView(
    LoginRequiredWithMessageMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Status
    success_message = _("Status has been successfully deleted")
    template_name = "statuses/delete.html"
    success_url = reverse_lazy("statuses_index")
