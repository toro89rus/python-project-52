from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.labels.forms import LabelsForm
from task_manager.labels.models import Label
from task_manager.mixins import RestrictStatusDeletionMixin


class LabelIndexView(ListView):
    queryset = Label.objects.all().order_by("id")
    template_name = "labels/index.html"
    context_object_name = "labels"


class LabelCreateView(SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelsForm
    success_message = _("Label has been successfully registered")
    template_name = "labels/create.html"
    success_url = reverse_lazy("labels_index")


class LabelUpdateView(
    SuccessMessageMixin,
    UpdateView,
):
    model = Label
    form_class = LabelsForm
    success_message = _("Label has been successfully updated")
    template_name = "labels/update.html"
    success_url = reverse_lazy("labels_index")


class LabelDeleteView(
    RestrictStatusDeletionMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Label
    success_message = _("Label has been successfully deleted")
    template_name = "labels/delete.html"
    success_url = reverse_lazy("labels_index")
