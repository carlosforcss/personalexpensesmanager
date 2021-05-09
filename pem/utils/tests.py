# -*- coding: utf-8 -*-
# Django
from django.test import TestCase, Client
# Third Parties
from faker import Faker
# Project
from pem.users.models import User


class BaseTestCase(TestCase):

    fake = Faker()

    def create_user(self, is_superuser=False, is_staff=False):
        password = self.fake.password()
        user = User.objects.create_user(
            username=self.fake.profile(fields=['username']).get("username"),
            first_name=self.fake.first_name(),
            last_name=self.fake.last_name(),
            email=self.fake.email(),
            phone=self.fake.phone_number(),
            is_superuser=is_superuser,
            is_staff=is_staff,
            password=password,
        )
        return user, password

    def create_superuser(self):
        return self.create_user(is_superuser=True, is_staff=True)

    def create_logged_client(self):
        user, password = self.create_user()
        client = Client()
        response = client.post("/get_token/", dict(username=user.username, password=password))
        token = response.data.get("token")
        client.token = token
        return client, user
