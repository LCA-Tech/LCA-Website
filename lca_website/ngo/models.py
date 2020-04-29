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
    A model to represent an NGO. The Registration number of the NGO is used as the primary key in the database.
    Since the category is chosen from a set of categories, it is made into an enum and stored as an integer.
    The website is made an optional field.
    The NGO is unapproved when added and has to be approved by the administrators.
    """

    name = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=25, primary_key=True)
    category = models.IntegerField(default=0, choices=NgoCategories.choices())
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=10)
    email_address = models.CharField(max_length=255)
    website = models.CharField(max_length=75, null=True)
    approved = models.BooleanField(default=False)
