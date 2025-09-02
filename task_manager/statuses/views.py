from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.mixins import RestrictStatusDeletionMixin


class StatusIndexView(ListView):
    queryset = Status.objects.all().order_by("id")
    template_name = "statuses/index.html"
    context_object_name = "statuses"


class StatusCreateView(SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    success_message = _("Status has been successfully registered")
    template_name = "statuses/create.html"
    success_url = reverse_lazy("statuses_index")


class StatusUpdateView(
    SuccessMessageMixin,
    UpdateView,
):
    model = Status
    form_class = StatusForm
    success_message = _("Status has been successfully updated")
    template_name = "statuses/update.html"
    success_url = reverse_lazy("statuses_index")


class StatusDeleteView(
    RestrictStatusDeletionMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Status
    success_message = _("Status has been successfully deleted")
    template_name = "statuses/delete.html"
    success_url = reverse_lazy("statuses_index")
