from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View


class MainView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = "login.html"
    next_page = reverse_lazy("main")
    success_message = _("You are logged in")


class UserLogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, _("You've successfully logged out"))
        return redirect(reverse("main"))
