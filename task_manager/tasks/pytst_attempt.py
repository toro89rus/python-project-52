import pytest

from django.core.management import call_command


@pytest.fixture(scope="module")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "users.json", "statuses.json", "tasks.json")


import pytest
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from pytest_django.asserts import assertContains, assertRedirects

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User

login_url = reverse("login")
index_tasks_url = reverse("tasks_index")
index_tasks_filter_status_url = reverse("tasks_index", query={"status": 2})
index_tasks_filter_executor_url = reverse("tasks_index", query={"executor": 2})
index_tasks_filter_self_tasks_url = reverse(
    "tasks_index", query={"self_tasks": "on"}
)
index_tasks_filter_full_url = reverse(
    "tasks_index", query={"status": 1, "executor": 1, "self_tasks": "on"}
)
create_tasks_url = reverse("tasks_create")
update_tasks_url = reverse("tasks_update", kwargs={"pk": 3})
delete_tasks_url = reverse("tasks_delete", kwargs={"pk": 1})
detail_tasks_url = reverse("tasks_detail", kwargs={"pk": 1})

task_urls = (
    index_tasks_url,
    create_tasks_url,
    update_tasks_url,
    delete_tasks_url,
    detail_tasks_url,
)

testuser_username = "user2"
testuser_password = "123"


@pytest.fixture
def logged_in_client(client):
    client.login(username=testuser_username, password=testuser_password)
    return client


@pytest.mark.parametrize("url", task_urls)
def test_tasks_without_login(client, url):
    response = client.get(url)
    assertRedirects(response, login_url)


@pytest.mark.django_db
def test_tasks_index(logged_in_client):
    response = logged_in_client.get(index_tasks_url)
    assert response.status_code == 200
    assertContains(response, _("Status"))
    assertContains(response, _("Executor"))
    assertContains(response, _("Author"))
    context = response.context
    assert len(context["tasks"]) == 4


@pytest.mark.django_db
def test_tasks_index_filter_status(logged_in_client):
    response = logged_in_client.get(index_tasks_filter_status_url)
    assert response.status_code == 200
    context = response.context
    assert len(context["tasks"]) == 2


@pytest.mark.django_db
def test_tasks_index_filter_executor(logged_in_client):
    response = logged_in_client.get(index_tasks_filter_executor_url)
    assert response.status_code == 200
    context = response.context
    assert len(context["tasks"]) == 2


@pytest.mark.django_db
def test_tasks_index_filter_self_tasks_false(logged_in_client):
    response = logged_in_client.get(index_tasks_filter_self_tasks_url)
    assert response.status_code == 200
    context = response.context
    assert len(context["tasks"]) == 1


@pytest.mark.django_db
def test_tasks_create_and_filter_self_tasks(logged_in_client):
    response = logged_in_client.post(
        create_tasks_url,
        data={
            "name": "New task",
            "description": "New description",
            "status": 1,
            "executor": 1,
        },
        follow=True,
    )
    assertRedirects(response, index_tasks_url)
    context = response.context
    assert len(context["tasks"]) == 5
    assertContains(response, "New task")


@pytest.mark.django_db
def test_tasks_update_tasks(logged_in_client):
    response = logged_in_client.post(
        update_tasks_url,
        data={
            "name": "Updated task",
            "description": "New description",
            "status": 1,
            "executor": 1,
        },
        follow=True,
    )
    assertRedirects(response, index_tasks_url)
    context = response.context
    assert len(context["tasks"]) == 4
    assertContains(response, "Updated task")
