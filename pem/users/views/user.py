# -*- coding: utf -8 -*-
# Django
# - - -
# Third Parties
from rest_framework import viewsets
# Project
from pem.users.models import User
from pem.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
