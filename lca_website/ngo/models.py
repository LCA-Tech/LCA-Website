from django.db import models
from enum import IntEnum


class NgoCategories(IntEnum):
    TYPE_ZERO_NGO = 0
    TYPE_ONE_NGO = 1

    @classmethod
    def choices(cls):
        return [(key.value, key.value) for key in cls]


class Ngo(models.Model):
    """
    """

    name = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=25, null=True)
    category = models.IntegerField(default=0, choices=NgoCategories.choices())
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=10)
    email_address = models.CharField(max_length=255)
    website = models.CharField(max_length=75, null=True)
    approved = models.BooleanField(default=False)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
            return self.name
