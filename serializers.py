from employer.models import Employer

from rest_framework import serializers

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'

    def validate_first_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("First name must be at least 3 characters long")
        return value

    def validate_last_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Last name must be at least 3 characters long")
        return value

    def validate_email(self, value):
        if not value.endswith('@example.com'):
            raise serializers.ValidationError("Email must be from example.com domain")
        return value

