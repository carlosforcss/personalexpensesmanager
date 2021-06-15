# -*- coding: utf-8 -*-
# Django
from django.test import TestCase, Client
# Third Parties & Python
from faker import Faker
from random import randrange
# Project
from pem.users.models import User


def _client_logged_required_decorator(func):
    def helper(self, *args, **kwargs):
        if not getattr(self, "_token", None):
            raise Exception("UserClient instance has to have _token property.")
        return func(self, *args, HTTP_AUTHORIZATION="Token {}".format(self._token), **kwargs)
    return helper


class UserClient(Client):

    MULTIPART_CONTENT = "application/json"
    user: User = None
    _token: str = None

    def __init__(self, user, password):
        super(UserClient, self).__init__()
        self.user = user
        response = super(UserClient, self).post("/get_token/", dict(
            username=user.username, password=password))
        self._token = token = response.data.get("token")

    @_client_logged_required_decorator
    def get(self, *args, **kwargs):
        return super(UserClient, self).get(*args, **kwargs)

    @_client_logged_required_decorator
    def post(self, *args, **kwargs):
        return super(UserClient, self).post(*args, content_type=self.MULTIPART_CONTENT, **kwargs)

    @_client_logged_required_decorator
    def put(self, *args, **kwargs):
        return super(UserClient, self).put(*args, content_type=self.MULTIPART_CONTENT, **kwargs)

    @_client_logged_required_decorator
    def delete(self, *args, **kwargs):
        return super(UserClient, self).delete(*args, **kwargs)


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
        client = UserClient(user, password)
        return client

    def get_random_choice(self, choices):
        random_number = randrange(0, len(choices) - 1)
        return choices[random_number][0]
