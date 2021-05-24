# -*- coding: utf-8 -*-
# Django
# - - -
# Third Parties
# - - -
# Project
from pem.balance.models import Concept, Category
from pem.utils.tests import BaseTestCase


class ConceptTestCase(BaseTestCase):
    client = None
    URL = "/api/balance/concept/"

    def setUp(self):
        self.client = self.create_logged_client()

    def test_create_concept(self):
        concept_name = self.fake.word()
        new_category = Category.objects.create(
            name=self.fake.word(),
            owner=self.client.user,
        )
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
