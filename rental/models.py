from django.db import models
from car.models import Car
from customer.models import Customer


class RentalManager(models.Manager):
    def total_revenue(self, start_date, end_date):
        return self.filter(start_date__gte=start_date, end_date__lte=end_date).aggregate(sum('total_price'))

class Rental(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True,related_name='rental')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True,related_name='rental')
    start_date = models.DateField(auto_now_add=False, null=False)
    end_date = models.DateField(auto_now_add=False, null=False)
    objects = RentalManager()

    def save(self, *args, **kwargs):
        self.car.available = False
        self.car.save()
        super(Rental, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.car.available = True
        self.car.save()
        super(Rental, self).delete(*args, **kwargs)

    @property
    def total_amount(self):
        return self.car.cost_per_day * (self.end_date - self.start_date).days

    def __str__(self):
        return str(self.car) + '-' + str(self.customer)



