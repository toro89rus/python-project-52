from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class LoginRequiredWithMessageMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(request, _("You're not authorised. Please login"))
        return super().dispatch(request, *args, **kwargs)


class OwnProfileMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.id == self.get_object().id

    def handle_no_permission(self):
        messages.error(self.request, _("You can't edit other user"))
        return redirect(reverse_lazy("users_index"))
