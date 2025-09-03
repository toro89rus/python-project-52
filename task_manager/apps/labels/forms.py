from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from task_manager.apps.labels.models import Label


class LabelsForm(ModelForm):

    class Meta:
        model = Label
        fields = ["name"]
        labels = {"name": _("Name")}
