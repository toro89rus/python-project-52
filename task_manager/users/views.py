from task_manager.users.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.users.forms import UserForm
from task_manager.mixins import OwnProfileMixin
from django.contrib.auth.decorators import login_not_required
from django.utils.decorators import method_decorator


@method_decorator(login_not_required, name="dispatch")
class UserIndexView(ListView):
    queryset = User.objects.all().order_by("id")
    template_name = "users/index.html"
    context_object_name = "users"


@method_decorator(login_not_required, name="dispatch")
class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    success_message = _("User has been successfully registered")
    template_name = "users/create.html"
    success_url = reverse_lazy("login")


class UserUpdateView(
    OwnProfileMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = User
    form_class = UserForm
    success_message = _("User has been successfully updated")
    template_name = "users/update.html"
    success_url = reverse_lazy("users_index")


class UserDeleteView(
    OwnProfileMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = User
    success_message = _("User has been successfully deleted")
    template_name = "users/delete.html"
    success_url = reverse_lazy("users_index")
