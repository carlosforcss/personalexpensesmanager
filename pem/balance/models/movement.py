# -*- coding: utf-8 -*-
# Django
from django.db import models
# Third Parties
# - - -
# Project
from pem.users.models import UserBasedModel


class Movement(UserBasedModel):

    concept = models.ForeignKey(
        "balance.Concept", on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name="movements"
    )
    amount = models.DecimalField(max_digits=11, decimal_places=2)

    class Meta:
        db_table = "movements"
