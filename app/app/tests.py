from django.test import TestCase
from app.calc import add


class CalcTests(TestCase):
    """Define: calc module tests"""
    def test_add_numbers(self):
        """It: should add two numbers"""
        self.assertEqual(add(5, 3), 8)
        