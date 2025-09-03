from django.test import TestCase
from django.urls import reverse

from task_manager.core import text_constants
from task_manager.statuses.models import Status


class StatusesTest(TestCase):
    fixtures = ["statuses.json", "users.json"]
    expected_statuses_count = 3
    test_status_id = 2
    testuser_username = "user2"
    testuser_password = "123"

    login_url = reverse("login")
    index_statuses_url = reverse("statuses_index")
    create_status_url = reverse("statuses_create")
    update_status_url = reverse(
        "statuses_update", kwargs={"pk": test_status_id}
    )
    delete_status_url = reverse(
        "statuses_delete", kwargs={"pk": test_status_id}
    )

    def setUp(self):
        self.client.login(
            username=self.testuser_username, password=self.testuser_password
        )

    def test_status_index(self):
        response = self.client.get(self.index_statuses_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("statuses", response.context)
        actual_statuses_count = len(response.context["statuses"])
        self.assertEqual(actual_statuses_count, self.expected_statuses_count)

    def test_status_create(self):
        response = self.client.post(
            self.create_status_url,
            data={"name": "Awaiting orders"},
            follow=True,
        )
        self.assertRedirects(response, self.index_statuses_url)
        self.assertContains(response, text_constants.STATUS_CREATED)
        self.assertContains(response, "Awaiting orders")
        actual_statuses_count = len(response.context["statuses"])
        self.assertEqual(
            actual_statuses_count, self.expected_statuses_count + 1
        )

    def test_status_update(self):
        response = self.client.post(
            self.update_status_url,
            data={
                "name": "Awaiting orders",
            },
            follow=True,
        )
        self.assertRedirects(response, self.index_statuses_url)
        self.assertContains(response, text_constants.STATUS_UPDATED)
        self.assertContains(response, "Awaiting orders")
        actual_statuses_count = len(response.context["statuses"])
        self.assertEqual(actual_statuses_count, self.expected_statuses_count)

    def test_status_delete(self):
        status = Status.objects.get(id=self.test_status_id)
        response = self.client.get(self.delete_status_url, follow=True)
        delete_confirm_message = text_constants.DELETE_CONFIRM % {
            "name": status.name
        }
        self.assertContains(response, delete_confirm_message)
        response = self.client.post(self.delete_status_url, follow=True)
        self.assertRedirects(response, self.index_statuses_url)
        self.assertContains(response, text_constants.STATUS_DELETED)
        actual_statuses_count = len(response.context["statuses"])
        self.assertEqual(
            actual_statuses_count, self.expected_statuses_count - 1
        )


class UnAuthenticatedStatusesTest(TestCase):
    login_url = reverse("login")
    index_statuses_url = reverse("statuses_index")

    def test_status_index(self):
        response = self.client.get(self.index_statuses_url, follow=True)
        self.assertRedirects(response, self.login_url)
        self.assertContains(response, text_constants.LOGIN_REQUIRED)
