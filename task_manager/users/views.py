from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView

from task_manager.users.forms import UserCreateForm


class IndexView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreateForm
    success_message = _("User has been successfully registered")
    template_name = "users/create.html"
    success_url = reverse_lazy("login")
