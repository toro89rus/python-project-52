from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label


class StatusesTest(TestCase):
    fixtures = ["labels.json", "users.json"]
    expected_labels_count = 3
    test_label_id = 2
    testuser_username = "user4"
    testuser_password = "123"
    create_message = _("Label has been successfully created")
    update_message = _("Label has been successfully updated")
    delete_confirm_message = "Do you really want to delete %(name)s?"
    delete_message = _("Label has been successfully deleted")

    login_url = reverse("login")
    labels_index_url = reverse("labels_index")
    labels_create_url = reverse("labels_create")
    labels_update_url = reverse("labels_update", kwargs={"pk": test_label_id})
    labels_delete_url = reverse("labels_delete", kwargs={"pk": test_label_id})

    def setUp(self):
        user = get_user_model()
        user.objects.create_user(
            username=self.testuser_username, password=self.testuser_password
        )
        self.client.login(
            username=self.testuser_username, password=self.testuser_password
        )

    def test_labels_index(self):
        response = self.client.get(self.labels_index_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("labels", response.context)
        actual_labels_count = len(response.context["labels"])
        self.assertEqual(actual_labels_count, self.expected_labels_count)

    def test_labels_create(self):
        response = self.client.post(
            self.labels_create_url,
            data={"name": "Testing"},
            follow=True,
        )
        self.assertRedirects(response, self.labels_index_url)
        self.assertContains(response, "Testing")
        actual_labels_count = len(response.context["labels"])
        self.assertEqual(actual_labels_count, self.expected_labels_count + 1)

    def test_labels_update(self):
        response = self.client.post(
            self.labels_update_url,
            data={
                "name": "Bug fixing",
            },
            follow=True,
        )
        self.assertRedirects(response, self.labels_index_url)
        self.assertContains(response, self.update_message)
        self.assertContains(response, "Bug fixing")
        actual_labels_count = len(response.context["labels"])
        self.assertEqual(actual_labels_count, self.expected_labels_count)

    def test_labels_delete(self):
        label = Label.objects.get(id=self.test_label_id)
        response = self.client.get(self.labels_delete_url, follow=True)
        delete_confirm_message = _(self.delete_confirm_message) % {
            "name": label.name
        }
        self.assertContains(response, delete_confirm_message)
        response = self.client.post(self.labels_delete_url, follow=True)
        self.assertRedirects(response, self.labels_index_url)
        self.assertContains(response, self.delete_message)
        actual_labels_count = len(response.context["labels"])
        self.assertEqual(actual_labels_count, self.expected_labels_count - 1)


class UnAuthenticatedLabelsTest(TestCase):
    login_url = reverse("login")
    labels_index_url = reverse("labels_index")

    def test_labels_index(self):
        response = self.client.get(self.labels_index_url)
        self.assertRedirects(response, self.login_url)
