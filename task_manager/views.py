from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin


class MainView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = "login.html"
    next_page = reverse_lazy("main")
    success_message = _("You are logged in")
