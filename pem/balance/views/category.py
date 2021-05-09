# -*- coding: utf-8 -*-
# Django
# - - -
# THird Parties
from rest_framework.viewsets import ModelViewSet
# Project
from pem.balance.models import Category
from pem.balance.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

