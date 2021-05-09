# -*- coding: utf -8 -*-
# Django
# - - -
# Third Parties
from rest_framework.routers import DefaultRouter
# Project
from pem.users.views import UserViewSet

router = DefaultRouter()
router.register("user", UserViewSet)
