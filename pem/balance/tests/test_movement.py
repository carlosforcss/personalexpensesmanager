# -*- coding: utf-8 -*-
# Django
# - - -
# Python & Third Parties
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList
from decimal import Decimal
from rest_framework import status
# Project
from pem.balance.models import Concept, Category, Movement
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
            is_periodical=True,
            type=self.get_random_choice(Concept.TYPES),
            period=self.get_random_choice(Concept.PERIODS),
            priority=self.get_random_choice(Concept.PRIORITIES),
            owner=self.client.user,
        )
        new_movement_data = dict(
            concept=dict(id=new_concept.id),
            amount=Decimal("10.00"),
        )
        response = self.client.post(self.URL, new_movement_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movement.objects.all().count(), 1)
        new_movement = Movement.objects.first()
        self.assertEqual(new_movement.amount, new_movement_data.get("amount"))
        self.assertEqual(new_movement.concept_id, new_concept.id)

        # Get Movement
        get_response = self.client.get("{}{}/".format(self.URL, new_movement.id))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(get_response.data), ReturnDict)
        self.assertEqual(get_response.data.get("id"), new_movement.id)

        # List Response
        list_response = self.client.get(self.URL)
        self.assertEqual(list_response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(list_response.data), ReturnList)
        self.assertEqual(len(list_response.data), 1)
        self.assertEqual(list_response.data[0].get("id"), new_movement.id)

        # Update Response
        update_data = dict(amount=Decimal("12.00"))
        update_response = self.client.put("{}{}/".format(self.URL, new_movement.id), update_data)
        self.assertEqual(update_response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(update_response.data), ReturnDict)
        self.assertEqual(update_response.data.get("amount"), "{}".format(update_data.get("amount")))

        # Remove Response
        remove_response = self.client.delete("{}{}/".format(self.URL, new_movement.id))
        self.assertEqual(remove_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movement.objects.all().exists())
