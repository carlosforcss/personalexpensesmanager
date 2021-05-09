# -*- coding: utf-8 -*-
# Django
# - - -
# THird Parties
from rest_framework.viewsets import ModelViewSet
# Project
from pem.balance.models import Concept
from pem.balance.serializers import ConceptSerializer


class ConceptViewSet(ModelViewSet):

    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer
