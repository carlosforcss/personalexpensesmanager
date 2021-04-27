# -*- coding: utf-8 -*-
# Django
from django.db import models
# Third Parties
# - - -
# Project
from pem.users.models import UserBasedModel


class Category(UserBasedModel):

    name = models.CharField(max_length=50)

    class Meta:
        db_table = "categories"
