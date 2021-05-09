# -*- coding: utf -8 -*-
# Django
# - - -
# Third Parties
from rest_framework import serializers
# Project
from pem.users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "phone",
            "first_name",
            "last_name",
        )

