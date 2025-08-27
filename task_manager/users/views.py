from django.views.generic import ListView
from task_manager.users.models import User


class IndexView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


