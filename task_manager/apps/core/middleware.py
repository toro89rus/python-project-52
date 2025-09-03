from django.contrib import messages
from django.contrib.auth.middleware import LoginRequiredMiddleware

from task_manager.apps.core import text_constants


class LoginRequiredWithMessageMiddleware(LoginRequiredMiddleware):
    redirect_field_name = None

    def handle_no_permission(self, request, view_func):
        messages.error(request, text_constants.LOGIN_REQUIRED)
        return super().handle_no_permission(request, view_func)
