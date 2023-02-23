from reservation.models import Reservation
from rest_framework import serializers

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        start_date = data.get('start_date', None)
        end_date = data.get('end_date', None)

        if start_date and end_date and start_date >= end_date:
            raise serializers.ValidationError("End date must be after start date")
        return data


