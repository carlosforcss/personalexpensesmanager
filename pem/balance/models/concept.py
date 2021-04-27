# -*- coding: utf-8 -*-
# Django
from django.db import models
# Third Parties
# - - -
# Project
from pem.users.models import UserBasedModel


class Concept(UserBasedModel):

    CRITICAL = 1
    HIGH = 2
    NORMAL = 3
    LOW = 4

    PIORITIES = (
        (CRITICAL, "Critical"),
        (HIGH, "High"),
        (NORMAL, "Normal"),
        (LOW, "Bajo"),
    )

    INGRESS = 1
    EGRESS = 2

    TYPES = (
        (INGRESS, "Ingress"),
        (EGRESS, "Egress"),
    )

    category = models.ForeignKey(
        "balance.Category", on_delete=models.CASCADE,
        related_name="concepts"
    )
    is_periodical = models.BooleanField(default=False)
    time_period = models.ForeignKey(
        "balance.TimePeriod", on_delete=models.SET_NULL,
        related_name="time_period",
        null=True, blank=True,
    )
    piority = models.SmallIntegerField(choices=PIORITIES, default=NORMAL)
    type = models.SmallIntegerField(choices=TYPES, default=EGRESS)
    default_amount = models.DecimalField(
        max_digits=11, decimal_places=2,
        null=True, blank=True,
    )

    class Meta:
        db_table = "concepts"
