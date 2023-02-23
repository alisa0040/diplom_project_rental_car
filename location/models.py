from django.db import models
from car.models import Car

class Location(models.Model):
    city = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    cars = models.ManyToManyField(Car, blank=True)

    def __str__(self):
        return self.city

