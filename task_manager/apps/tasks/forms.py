import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.apps.labels.models import Label
from task_manager.apps.tasks.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "label"]


class TaskFilterForm(django_filters.FilterSet):

    class Meta:
        model = Task
        fields = ["status", "executor"]

    label = django_filters.ModelChoiceFilter(
            queryset=Label.objects.all(), label=_("Label")
        )

    self_tasks = django_filters.BooleanFilter(
        widget=forms.CheckboxInput,
        method="filter_self_tasks",
        label=_("Own tasks only"),
    )

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
