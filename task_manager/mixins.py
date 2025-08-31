from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class PermissionDeniedMixin(UserPassesTestMixin):
    error_message = "You don't have permission to do this"
    redirect_url = "main"

    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            messages.error(request, _(self.error_message))
            return redirect(reverse_lazy(self.redirect_url))
        return super().dispatch(request, *args, **kwargs)


class OwnProfileMixin(PermissionDeniedMixin):
    error_message = "You can't edit other user"
    redirect_url = "users_index"

    def test_func(self):
        return self.request.user.id == self.get_object().id


class OwnTaskMixin(PermissionDeniedMixin):
    error_message = "Only author have permission to delete task"
    redirect_url = "tasks_index"

    def test_func(self):
        return self.request.user.id == self.get_object().author_id
