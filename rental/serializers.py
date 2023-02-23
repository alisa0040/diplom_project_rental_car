from rental.models import Rental
from rest_framework import serializers

class RentalSerializer(serializers.ModelSerializer):
    total_amount = serializers.ReadOnlyField()

    class Meta:
        model = Rental
        fields = '__all__'
