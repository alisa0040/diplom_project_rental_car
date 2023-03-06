from rental.models import Rental
from rest_framework import serializers
from car.serializers import CarSerializer

class RentalSerializer(serializers.ModelSerializer):
    total_amount = serializers.FloatField(read_only=True)

    class Meta:
        model = Rental
        fields = '__all__'
