# -*- coding: utf-8 -*-
# Django
# - - -
# Third Parties
# - - -
# Project
from pem.balance.models import Movement, Concept
from pem.utils.serializers import UserBasedSerializer
from pem.utils.serializers import CustomSlugRelatedField


class MovementSerializer(UserBasedSerializer):

    concept = CustomSlugRelatedField(
        queryset=Concept.objects.all(),
        slug_field="id",
        required=True,
        allow_null=False,
    )

    class Meta:

        model = Movement
        fields = ("id", "amount", "concept")
