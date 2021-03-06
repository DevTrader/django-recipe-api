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

    def test_new_user_invalid_email(self):
        """Should error when creating user without email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password="randompass"
            )

    def test_create_new_superuser(self):
        """Should create superuser"""
        user = get_user_model().objects.create_superuser(
            "superuser@email.com",
            "superuserrandompass"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
