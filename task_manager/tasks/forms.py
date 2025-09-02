from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor"]


class TaskFilterForm(forms.Form):

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(), required=False
    )
    executor = forms.ModelChoiceField(
        queryset=User.objects.all(), required=False
    )
    self_tasks = forms.BooleanField(required=False, label=_("Own tasks only"))
