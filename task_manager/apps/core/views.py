from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth.decorators import login_not_required
from django.utils.decorators import method_decorator

from task_manager.apps.core import text_constants


@method_decorator(login_not_required, name="dispatch")
class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "core/main.html")


@method_decorator(login_not_required, name="dispatch")
class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = "core/login.html"
    next_page = reverse_lazy("main")
    success_message = text_constants.LOGIN


@method_decorator(login_not_required, name="dispatch")
class UserLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, text_constants.LOGOUT)
        return redirect(reverse("main"))
