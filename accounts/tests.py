from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username = "user1",
            password = "pass-123",
            email = "user-1@gmail.com"
        )

    def test_save_user_object_to_model(self):
        self.assertEqual(self.user.username, "user1")
        self.assertEqual(self.user.email, "user-1@gmail.com")