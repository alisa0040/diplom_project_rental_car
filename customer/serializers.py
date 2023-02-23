from rest_framework import serializers
from django.core.exceptions import ValidationError
from customer.models import Customer
import re


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'

    def validate_first_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('First name cannot be blank.')
        return value

    def validate_last_name(self, value):
        if not value.strip():
            raise serializers.ValidationError('Last name cannot be blank.')
        return value

    def validate_email(self, value):
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
            raise serializers.ValidationError('Email format is invalid.')
        return value

    def validate_phone_number(self, value):
        if not re.match(r'^\d{10}$', value):
            raise serializers.ValidationError('Phone number format is invalid.')
        return value
