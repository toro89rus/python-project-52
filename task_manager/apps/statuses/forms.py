from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from task_manager.apps.statuses.models import Status


class StatusForm(ModelForm):

    class Meta:
        model = Status
        fields = ["name"]
        labels = {"name": _("Name")}
