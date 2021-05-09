from django.test import TestCase


class UserTestCase(TestCase):

    def test_login(self):
        print("my test is working")
        self.assertEqual(True, True)
