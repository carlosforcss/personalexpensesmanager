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

    ANNUAL = 1
    MONTHLY = 2
    WEEKLY = 3
    DAILY = 4

    PERIODS = (
        (ANNUAL, "Annual"),
        (MONTHLY, "Monthly"),
        (WEEKLY, "Weekly"),
        (DAILY, "Daily"),
    )

    category = models.ForeignKey(
        "balance.Category", on_delete=models.CASCADE,
        related_name="concepts"
    )
    is_periodical = models.BooleanField(default=False)
    piority = models.SmallIntegerField(choices=PIORITIES, default=NORMAL)
    type = models.SmallIntegerField(choices=TYPES, default=EGRESS)
    default_amount = models.DecimalField(
        max_digits=11, decimal_places=2,
        null=True, blank=True,
    )

    period = models.SmallIntegerField(choices=PERIODS, default=MONTHLY)
    period_interval = models.SmallIntegerField(default=1)

    class Meta:
        db_table = "concepts"
