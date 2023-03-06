from django.db import models
from django.utils import timezone
from employer.models import Employer


class CarManager(models.Manager):
    def available(self):
        return self.filter(is_available=True)

    def available_on_date(self, start_date, end_date):
        return self.filter(is_available=True, rentals__end_date__gte=start_date,
                           rentals__start_date__lte=end_date).distinct()


class CarBrand(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FuelType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CarOption(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class CarTransmission(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, null=True, related_name='cars')
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, null=True, related_name='cars')
    transmission = models.ForeignKey(CarTransmission, on_delete=models.CASCADE, null=True, related_name='cars')
    fueltype = models.ForeignKey(FuelType, on_delete=models.CASCADE, null=True, related_name='cars')
    options = models.ManyToManyField(CarOption, blank=True)
    year = models.IntegerField(verbose_name='Year')
    color = models.CharField(max_length=255, verbose_name='Color')
    cost_per_day = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='cost per day $', default=0.0,
                                       null=True)
    is_employer = models.ForeignKey(Employer, on_delete=models.CASCADE, null=True)
    available = models.BooleanField(default=True)
    objects = CarManager()

    def __str__(self):
        return str(self.brand) + '-' + str(self.car_model) + '-' + str(self.is_employer)

class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, related_name='car_image')
    image = models.ImageField(upload_to='car_images/')
    caption = models.CharField(max_length=200, blank=True, null=True)

