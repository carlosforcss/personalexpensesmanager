# -*- coding: utf-8 -*-
# Django
# - - -
# THird Parties
from rest_framework.serializers import ModelSerializer
# Project
from pem.balance.models import Movement


class MovementSerializer(ModelSerializer):

    class Meta:

        model = Movement
        fields = ("id", "amount", "concept")
