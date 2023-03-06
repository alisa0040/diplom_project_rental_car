from django.db import models

from car.models import Car
from customer.models import Customer

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True,related_name='reservation')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True,related_name='reservation')
    start_date = models.DateField(auto_now_add=False, null=False)
    end_date = models.DateField(auto_now_add=False, null=False)

    def save(self, *args, **kwargs):
        self.car.available = False
        self.car.save()
        super(Reservation, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.car.available = True
        self.car.save()
        super(Reservation, self).delete(*args, **kwargs)
    def __str__(self):
        return str(self.car) + '-' + str(self.customer)
