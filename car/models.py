from django.db import models
from agency.models import Agency

# Car model definition
class Car(models.Model):
    CAR_TYPE_CHOICES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("TRUCK", "Truck"),
        ("VAN", "Van"),
        ("OTHER", "Other"),
    ]

    name = models.CharField(max_length=255, null=False, blank=False)
    car_type = models.CharField(
        max_length=50,
        choices=CAR_TYPE_CHOICES,
        default="SEDAN",
    )
    agency = models.ForeignKey(Agency, related_name='cars', on_delete=models.CASCADE)
    daily_rent = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f"{self.name} ({self.car_type})"