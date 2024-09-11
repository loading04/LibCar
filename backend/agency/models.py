from django.db import models
from django.db.models import CharField

# Create your models here.


class Agency(models.Model):

    AGENCY_TYPE_CHOICES = [
        ("LUX", "Luxury"),
        ("PICKUP", "Pickup"),
        ("NORMAL", "Normal"),
        ("OTHER", "Other"),
    ]
    name = CharField(max_length=255, null=False, blank=False)
    type = models.CharField(
        max_length=255,
        choices=AGENCY_TYPE_CHOICES,
        default="NORMAL",
    )
    location = CharField(max_length=255)

    class Meta:
        verbose_name = "Agency"
        verbose_name_plural = "Agencies"

    def __str__(self):
        return self.name
