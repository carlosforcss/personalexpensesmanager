# -*- coding: utf-8 -*-
# Django
# - - -
# Third Parties
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
# Project
from pem.balance.models import Concept, Category
from pem.utils.tests import BaseTestCase


class ConceptTestCase(BaseTestCase):
    client = None
    URL = "/api/balance/movement/"

    def setUp(self):
        self.client = self.create_logged_client()

    def test_crud_movement(self):
        new_category = Category.objects.create(
            name=self.fake.word(),
            owner=self.client.user,
        )
        new_concept = Concept.objects.create(
            category=new_category,
            name=self.fake.word(),
            is_periodical=False,
            priority=self.get_random_choice(Concept.PRIORITIES),
            type=self.get_random_choice(Concept.TYPES),
            period=self.get_random_choice(Concept.PERIODS),
        )
