from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from task_manager.apps.users.models import User


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
        ]
        labels = {
            "first_name": _("First name"),
            "last_name": _("Last Name"),
            "username": _("Username"),
        }
