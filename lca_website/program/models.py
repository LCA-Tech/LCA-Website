from django.db import models

class Program(models.Model):
    """
    """

    name = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    eligiblity_criteria = models.CharField(max_length=255, null=True)
    date = models.DateTimeField()
    venue = models.CharField(max_length=255)

    def __str__(self):
        return self.name
