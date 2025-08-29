from task_manager.core.views import MainView, UserLoginView, UserLogoutView
from django.urls import path

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
