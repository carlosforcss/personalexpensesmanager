# -*- coding: utf-8 -*-
# Django
# - - -
# Python & Third Parties
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
# Project
from pem.balance.models import Concept, Category
from pem.utils.tests import BaseTestCase
from decimal import Decimal


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
                "priority": Concept.NORMAL,
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
        get_response = self.client.get("{}{}/".format(self.URL, new_concept.id))
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(type(get_response.data), ReturnDict)
        self.assertEqual(get_response.data.get("id"), new_concept.id)

        # List concept
        list_response = self.client.get(self.URL)
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(type(list_response.data), ReturnList)
        self.assertEqual(len(list_response.data), 1)
        self.assertEqual(list_response.data[0].get("id"), new_concept.id)

        # Update concept
        new_default_amount = Decimal(self.fake.random_number()).quantize(Decimal("0.00"))
        update_response = self.client.put("{}{}/".format(self.URL, new_concept.id), dict(
            default_amount=new_default_amount))
        self.assertEqual(update_response.status_code, 200)
        self.assertEqual(type(update_response.data), ReturnDict)
        self.assertEqual(update_response.data.get("id"), new_concept.id)
        self.assertEqual(update_response.data.get("default_amount"), "{}".format(new_default_amount))

        # Remove concept
        delete_response = self.client.delete("{}{}/".format(self.URL, new_concept.id))
        self.assertEqual(delete_response.status_code, 204)
        self.assertFalse(Concept.objects.all().exists())
