# -*- coding: utf-8 -*-
# Django
# - - -
# THird Parties
from rest_framework.serializers import ModelSerializer
# Project
from pem.balance.models import Category
from pem.utils.serializers import UserBasedSerializer


class CategorySerializer(UserBasedSerializer):

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user if request else None
        new_category = super().create(validated_data)
        new_category.owner = user
        return new_category

    class Meta:
        model = Category
        fields = ("id", "name")
