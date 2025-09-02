from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.db.models import RestrictedError


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


class RedirectOnRestrictedDeletionMixin():
    error_message = "You can't delete this"
    redirect_url = "main"

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except RestrictedError:
            messages.error(
                self.request, _(self.error_message)
            )
            return redirect(reverse_lazy(self.redirect_url))


class RestrictStatusDeletionMixin(RedirectOnRestrictedDeletionMixin):
    error_message = "Can't delete, status is being used"
    redirect_url = "statuses_index"


class RestrictUserDeletionMixin(RedirectOnRestrictedDeletionMixin):
    error_message = "Can't delete, user is being used"
    redirect_url = "users_index"
