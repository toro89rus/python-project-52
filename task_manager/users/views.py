from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from task_manager.users.forms import UserCreateForm
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy


class IndexView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreateForm
    success_message = _("User has been successfully registered")
    template_name = "users/create.html"
    success_url = reverse_lazy("users_index")
