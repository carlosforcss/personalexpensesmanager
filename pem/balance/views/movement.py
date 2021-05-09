# -*- coding: utf-8 -*-
# Django
# - - -
# THird Parties
from rest_framework.viewsets import ModelViewSet
# Project
from pem.balance.models import Movement
from pem.balance.serializers import MovementSerializer


class MovementViewSet(ModelViewSet):

    queryset = Movement.objects.all()
    serializer_class = MovementSerializer
