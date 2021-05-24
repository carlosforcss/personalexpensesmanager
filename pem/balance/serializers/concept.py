# -*- coding: utf-8 -*-
# Django
# - - -
# THird Parties
from rest_framework import serializers
# Project
from pem.balance.models import Concept, Category
from pem.utils.serializers import UserBasedSerializer, CustomSlugRelatedField


class ConceptSerializer(UserBasedSerializer):

    category = CustomSlugRelatedField(
        slug_field="id",
        queryset=Category.objects.all()
    )

    def validate(self, data):
        is_periodical = data.get("is_periodical")
        period = data.get("period")

        if is_periodical and not period:
            raise serializers.ValidationError({
                "period": "If concept is periodical the period has to be defined"
            })

        return data

    class Meta:
        model = Concept
        fields = (
            "id",
            "category",
            "is_periodical",
            "piority",
            "default_amount",
            "type",
        )
