# -*- coding: utf-8 -*-
# Django
from django.test import TestCase
from django.test import Client
# Third Parties
# - - -
# Project
from pem.balance.models import Category
from pem.utils.tests import BaseTestCase


class CategoryTestCase(BaseTestCase):
    client = None
    URL = "/api/balance/category/"

    def setUp(self):
        self.client, _ = self.create_logged_client()

    def test_create_category(self):
        category_name = self.fake.word()
        response = self.client.post(
            "/api/balance/category/",
            dict(name=category_name),
            HTTP_AUTHORIZATION="Token {}".format(self.client.token),
        )
        self.assertEqual(response.status_code, 201)
        new_category = Category.objects.filter(name=category_name)
        self.assertTrue(new_category.exists())
