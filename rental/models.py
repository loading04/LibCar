from django.db import models
from car.models import Car
from django.contrib.auth.models import User


class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.FloatField()

    def CalculateTotalPrice(self):
        days = (self.end_date - self.start_date).days
        return self.car.daily_rent * days

    def save(self, *args, **kwargs):
        self.total_price = self.CalculateTotalPrice()
        super().save(*args, **kwargs)
