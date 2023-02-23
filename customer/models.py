from django.db import models

from users.models import User

class Customer(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    address = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,related_name='customer')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


