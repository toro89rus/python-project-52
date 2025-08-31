from django.contrib.auth.middleware import LoginRequiredMiddleware
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class LoginRequiredWithMessageMiddleware(LoginRequiredMiddleware):
    redirect_field_name = None

    def handle_no_permission(self, request, view_func):
        messages.error(request, _("You're not authorised. Please login"))
        return super().handle_no_permission(request, view_func)
