from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.db.models import RestrictedError
from django.shortcuts import redirect
from django.urls import reverse_lazy

from task_manager.apps.core import text_constants


class PermissionDeniedMixin(UserPassesTestMixin):
    error_message = "You don't have permission to do this"
    redirect_url = "main"

    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            messages.error(request, self.error_message)
            return redirect(reverse_lazy(self.redirect_url))
        return super().dispatch(request, *args, **kwargs)


class OwnProfileMixin(PermissionDeniedMixin):
    error_message = text_constants.USER_RESTRICT_UPDATE
    redirect_url = "users_index"

    def test_func(self):
        return self.request.user.id == self.get_object().id


class OwnTaskMixin(PermissionDeniedMixin):
    error_message = text_constants.TASK_RESTRICT_DELETE
    redirect_url = "tasks_index"

    def test_func(self):
        return self.request.user.id == self.get_object().author_id


class RedirectOnRestrictedDeletionMixin:
    error_message = "You can't delete this"
    redirect_url = "main"

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except RestrictedError:
            messages.error(self.request, self.error_message)
            return redirect(reverse_lazy(self.redirect_url))


class RestrictStatusDeletionMixin(RedirectOnRestrictedDeletionMixin):
    error_message = text_constants.STATUS_RESTRICT_DELETE
    redirect_url = "statuses_index"


class RestrictUserDeletionMixin(RedirectOnRestrictedDeletionMixin):
    error_message = text_constants.USER_RESTRICT_DELETE
    redirect_url = "users_index"


class RestrictLabelDeletionMixin(RedirectOnRestrictedDeletionMixin):
    error_message = text_constants.LABEL_RESTRICT_DELETE
    redirect_url = "labels_index"
