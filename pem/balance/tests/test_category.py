# -*- coding: utf-8 -*-
# Django
# - - -
# Third Parties
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
# Project
from pem.balance.models import Category
from pem.utils.tests import BaseTestCase


class CategoryTestCase(BaseTestCase):
    client = None
    URL = "/api/balance/category/"

    def setUp(self):
        self.client = self.create_logged_client()

    def test_crud_category(self):
        category_name = self.fake.word()

        # Create Category
        response = self.client.post(
            self.URL,
            dict(name=category_name),
        )
        self.assertEqual(response.status_code, 201)
        categories = Category.objects.filter(name=category_name)
        self.assertTrue(categories.exists())
        new_category = categories.first()
        self.assertEqual(new_category.owner.id, self.client.user.id)
        self.assertEqual(new_category.name, category_name)

        # Get Category
        get_response = self.client.get("{}{}/".format(self.URL, new_category.id))
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(type(get_response.data), ReturnDict)
        self.assertEqual(get_response.data.get("id"), new_category.id)

        # List Categories
        list_response = self.client.get(self.URL)
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(type(list_response.data), ReturnList)
        self.assertEqual(len(list_response.data), 1)
        self.assertEqual(list_response.data[0].get("id"), new_category.id)

        # Update Category
        new_name = self.fake.word()
        update_response = self.client.put(
            "{}{}/".format(self.URL, new_category.id),
            dict(name=new_name),
        )
        new_category.refresh_from_db()
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(type(update_response.data), ReturnDict)
        self.assertEqual(update_response.data.get("name"), new_name)
        self.assertEqual(new_category.name, new_name)

        # Delete Categories
        delete_response = self.client.delete("{}{}/".format(self.URL, new_category.id))
        self.assertEqual(delete_response.status_code, 204)
        self.assertFalse(Category.objects.all().exists())
