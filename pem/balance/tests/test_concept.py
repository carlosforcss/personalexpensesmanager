# -*- coding: utf-8 -*-
# Django
# - - -
# Python & Third Parties
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
# Project
from pem.balance.models import Concept, Category
from pem.utils.tests import BaseTestCase


class ConceptTestCase(BaseTestCase):
    client = None
    URL = "/api/balance/concept/"

    def setUp(self):
        self.client = self.create_logged_client()

    def test_crud_concept(self):
        concept_name = self.fake.word()
        new_category = Category.objects.create(
            name=self.fake.word(),
            owner=self.client.user,
        )
        # Create Concept
        response = self.client.post(
            self.URL,
            {
                "name": concept_name,
                "category": new_category.id,
                "is_periodical": False,
                "piority": Concept.NORMAL,
                "type": Concept.INGRESS,
                "default_amount": "{}".format(self.fake.random_number()),
            },
        )
        self.assertEqual(response.status_code, 201)
        concepts = Concept.objects.filter()
        self.assertTrue(concepts.exists())
        new_concept = concepts.first()
        self.assertEqual(new_concept.owner.id, self.client.user.id)

        # Get a concept
        get_response = self.client.get("{}{}".format(self.URL, new_concept.first()))
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_response.body, ReturnDict)
        self.assertEqual(get_response.body.get("id"), new_concept.id)

        # List concept
        list_response = self.client.get(self.URL)
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(list_response.body, ReturnList)
        self.assertEqual(len(list_response.body), 1)
        self.assertEqual(list_response[0].get("id"), new_concept.id)

        # Update concept
        new_default_amount = self.fake.random_number()
        update_response = self.client.get(self.URL, dict(
            default_amount=new_default_amount))
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(update_response.body, ReturnDict)
        self.assertEqual(update_response.get("id"), new_concept.id)
        self.assertEqual(update_response.get("default_amount"), new_default_amount)

        # Remove concept
        delete_response = self.client.delete("{}{}".format(self.URL, new_default_amount))
        self.assertEqual(delete_response.status_code, 200)
        self.assertFalse(Concept.objects.all().exists())
