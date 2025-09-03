from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.test import TestCase
from django.urls import reverse

from task_manager.core import text_constants


class UsersTest(TestCase):
    fixtures = ["users.json"]
    expected_users_count = 3
    test_user_id = 2
    testuser_username = "user2"
    testuser_password = "123"
    mismatched_passwords_message = UserCreationForm.error_messages[
        "password_mismatch"
    ]

    login_url = reverse("login")
    index_users_url = reverse("users_index")
    create_user_url = reverse("users_create")
    update_user_url = reverse("users_update", kwargs={"pk": test_user_id})
    update_wrong_user_url = reverse(
        "users_update", kwargs={"pk": test_user_id + 1}
    )
    delete_user_url = reverse("users_delete", kwargs={"pk": test_user_id})
    delete_wrong_user_url = reverse(
        "users_delete", kwargs={"pk": test_user_id + 1}
    )

    def test_user_index(self):
        response = self.client.get(self.index_users_url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("users", response.context)
        actual_users_count = len(response.context["users"])
        self.assertEqual(actual_users_count, self.expected_users_count)

    def test_user_create(self):
        response = self.client.post(
            self.create_user_url,
            data={
                "first_name": "John",
                "last_name": "Doe",
                "username": "john12",
                "password1": "123",
                "password2": "123",
            },
            follow=True,
        )
        self.assertRedirects(response, self.login_url)
        self.assertContains(response, text_constants.USER_CREATED)

        response = self.client.get(self.index_users_url)
        self.assertContains(response, "John Doe")
        actual_users_count = len(response.context["users"])
        self.assertEqual(actual_users_count, self.expected_users_count + 1)

    def test_user_create_not_matching_passwords(self):
        response = self.client.post(
            self.create_user_url,
            data={
                "first_name": "John",
                "last_name": "Doe",
                "username": "john12",
                "password1": "123",
                "password2": "321",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.mismatched_passwords_message)

    def test_user_update(self):
        self.client.login(
            username=self.testuser_username, password=self.testuser_password
        )
        response = self.client.post(
            self.update_user_url,
            data={
                "first_name": "Bob",
                "last_name": "Tompson",
                "username": "bob_18",
                "password1": "123",
                "password2": "123",
            },
            follow=True,
        )
        self.assertRedirects(response, self.index_users_url)
        self.assertContains(response, text_constants.USER_UPDATED)
        self.assertContains(response, "Bob Tompson")
        actual_users_count = len(response.context["users"])
        self.assertEqual(actual_users_count, self.expected_users_count)

    def test_wrong_user_update(self):
        self.client.login(
            username=self.testuser_username, password=self.testuser_password
        )
        response = self.client.get(self.update_wrong_user_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text_constants.USER_RESTRICT_UPDATE)

    def test_user_delete(self):
        User = get_user_model()
        user = User.objects.get(id=self.test_user_id)
        self.client.login(
            username=self.testuser_username, password=self.testuser_password
        )
        response = self.client.get(self.delete_user_url, follow=True)
        delete_confirm_message = text_constants.DELETE_CONFIRM % {
            "name": str(user)
        }
        self.assertContains(response, delete_confirm_message)
        response = self.client.post(self.delete_user_url, follow=True)
        self.assertRedirects(response, self.index_users_url)
        self.assertContains(response, text_constants.USER_DELETED)
        actual_users_count = len(response.context["users"])
        self.assertEqual(actual_users_count, self.expected_users_count - 1)
