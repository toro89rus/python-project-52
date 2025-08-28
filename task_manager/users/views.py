from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView, UpdateView

from task_manager.users.forms import UserForm


class IndexView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    success_message = _("User has been successfully registered")
    template_name = "users/create.html"
    success_url = reverse_lazy("login")


class UserUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = User
    form_class = UserForm
    success_message = _("User has been successfully updated")
    login_url = reverse_lazy("login")
    template_name = "users/update.html"
    success_url = reverse_lazy("users_index")

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(request, _("You're not authorised. Please login"))
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.id == self.get_object().id

    def handle_no_permission(self):
        messages.error(self.request, _("You can't edit other user"))
        return redirect(reverse_lazy("users_index"))
