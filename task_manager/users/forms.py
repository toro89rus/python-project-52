from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class UserForm(BaseUserCreationForm):

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
