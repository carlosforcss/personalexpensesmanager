# -*- coding: utf-8 -*-
# Django
# - - -
# THird Parties
from rest_framework.serializers import ModelSerializer
# Project
from pem.balance.models import Concept


class ConceptSerializer(ModelSerializer):

    class Meta:

        model = Concept
        fields = (
            "id",
            "cateogry",
            "is_periodical",
            "piority",
            "default_amount",
            "type"
        )
