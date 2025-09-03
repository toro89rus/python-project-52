from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.apps.core import text_constants
from task_manager.apps.tasks.models import Task


class TasksTest(TestCase):
    fixtures = ["users.json", "statuses.json", "tasks.json"]
    expected_tasks_count = 4
    test_task_id = 2
    delete_task_id = 5
    testuser_username = "user4"
    testuser_password = "123"

    login_url = reverse("login")
    tasks_index_url = reverse("tasks_index")
    tasks_create_url = reverse("tasks_create")
    tasks_update_url = reverse("tasks_update", kwargs={"pk": test_task_id})
    tasks_read_url = reverse("tasks_update", kwargs={"pk": test_task_id})
    tasks_delete_url = reverse("tasks_delete", kwargs={"pk": delete_task_id})

    def setUp(self):
        user = get_user_model()
        user.objects.create_user(
            username=self.testuser_username, password=self.testuser_password
        )
        self.client.login(
            username=self.testuser_username, password=self.testuser_password
        )

    def test_tasks_index(self):
        response = self.client.get(self.tasks_index_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("tasks", response.context)
        actual_tasks_count = len(response.context["tasks"])
        self.assertEqual(actual_tasks_count, self.expected_tasks_count)

    def test_tasks_create(self):
        response = self.client.post(
            self.tasks_create_url,
            data={
                "name": "New task",
                "description": "New description",
                "status": 1,
                "executor": 1,
            },
            follow=True,
        )
        self.assertRedirects(response, self.tasks_index_url)
        self.assertContains(response, text_constants.TASK_CREATED)
        self.assertContains(response, "New task")
        actual_tasks_count = len(response.context["tasks"])
        self.assertEqual(actual_tasks_count, self.expected_tasks_count + 1)

    def test_tasks_update(self):
        response = self.client.post(
            self.tasks_update_url,
            data={
                "name": "Updated task name",
                "description": "New description",
                "status": 1,
                "executor": 1,
            },
            follow=True,
        )
        self.assertRedirects(response, self.tasks_index_url)
        self.assertContains(response, text_constants.TASK_UPDATED)
        self.assertContains(response, "Updated task name")
        actual_tasks_count = len(response.context["tasks"])
        self.assertEqual(actual_tasks_count, self.expected_tasks_count)

    def test_tasks_delete(self):
        task_to_delete = Task.objects.create(
            name="Task_to_delete", status_id=1, executor_id=1, author_id=4
        )
        response = self.client.get(self.tasks_delete_url, follow=True)
        delete_confirm_message = text_constants.DELETE_CONFIRM % {
            "name": task_to_delete.name
        }
        self.assertContains(response, delete_confirm_message)
        response = self.client.post(self.tasks_delete_url, follow=True)
        self.assertRedirects(response, self.tasks_index_url)
        self.assertContains(response, text_constants.TASK_DELETED)
        actual_tasks_count = len(response.context["tasks"])
        self.assertEqual(actual_tasks_count, self.expected_tasks_count)


class UnAuthenticatedTasksTest(TestCase):
    login_url = reverse("login")
    index_tasks_url = reverse("tasks_index")

    def test_tasks_index(self):
        response = self.client.get(self.index_tasks_url, follow=True)
        self.assertRedirects(response, self.login_url)
        self.assertContains(response, text_constants.LOGIN_REQUIRED)
