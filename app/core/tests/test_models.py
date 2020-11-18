from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Should create a new user with email successfully"""
        email = "test@email.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Should normalize new user emails"""
        email = "noTnorMaLized@EmAIL.CoM"
        user = get_user_model().objects.create_user(
            email=email,
            password="randompass"
        )

        self.assertEqual(user.email, email.lower())
