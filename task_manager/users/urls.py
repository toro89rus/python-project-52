from django.urls import path

from task_manager.users.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="users_index"),
]
