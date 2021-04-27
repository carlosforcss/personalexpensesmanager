# -*- coding: utf-8 -*-
# Django
from django.db import models
# Third Parties
# - - -
# Project
from pem.users.models import UserBasedModel


class TimePeriod(UserBasedModel):

    ANNUAL = 1
    MONTHLY = 2
    WEEKLY = 3
    DAILY = 4

    TYPES = (
        (ANNUAL, "Annual"),
        (MONTHLY, "Monthly"),
        (WEEKLY, "Weekly"),
        (DAILY, "Daily"),
    )

    type = models.SmallIntegerField(choices=TYPES, default=MONTHLY)
    interval = models.SmallIntegerField()

    class Meta:
        db_table = "time_periods"
