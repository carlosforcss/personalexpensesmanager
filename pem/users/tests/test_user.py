# -*- coding: utf-8 -*-
# Django
from django.test import TestCase
from django.test import Client
# Third Parties
# - - -
# Project
from pem.users.models import User


class UserTestCase(TestCase):
    client = None

    def setUp(self):
        User.objects.create_user(
            username="root",
            password="root",
            first_name="Carlos",
            last_name="Sanchez",
            email="me@test.com",
            phone="421 232 23 12",
            is_staff=True,
            is_superuser=True,
        )
        self.client = Client()

    def test_right_credentials(self):
        response = self.client.post("/get_token/", data=dict(username="root", password="root"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data.get('token'))

    def test_wrong_credentials(self):
        response = self.client.post("/get_token/", data=dict(username="root", password="wrong"))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.get('token'), None)
