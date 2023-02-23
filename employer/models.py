from django.db import models

from users.models import User


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,related_name='employer')
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    address = models.TextField(null=True)


    class Meta:
        ordering=('name', )

    def __str__(self):
        return self.name


