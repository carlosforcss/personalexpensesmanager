# -*- coding: utf-8 -*-
# Django
# - - -
# Third Parties
from rest_framework.routers import DefaultRouter
# Project
from pem.balance.views import CategoryViewSet, ConceptViewSet, MovementViewSet

router = DefaultRouter()
router.register("category", CategoryViewSet)
router.register("concept", ConceptViewSet)
router.register("movement", MovementViewSet)
