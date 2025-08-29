from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.users.forms import UserForm
from task_manager.mixins import LoginRequiredWithMessageMixin, OwnProfileMixin


class UserIndexView(ListView):
    queryset = User.objects.all().order_by("id")
    template_name = "users/index.html"
    context_object_name = "users"


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    success_message = _("User has been successfully registered")
    template_name = "users/create.html"
    success_url = reverse_lazy("login")


class UserUpdateView(
    LoginRequiredWithMessageMixin,
    OwnProfileMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = User
    form_class = UserForm
    success_message = _("User has been successfully updated")
    login_url = reverse_lazy("login")
    template_name = "users/update.html"
    success_url = reverse_lazy("users_index")


class UserDeleteView(
    LoginRequiredWithMessageMixin,
    OwnProfileMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = User
    success_message = _("User has been successfully deleted")
    login_url = reverse_lazy("login")
    template_name = "users/delete.html"
    success_url = reverse_lazy("users_index")
