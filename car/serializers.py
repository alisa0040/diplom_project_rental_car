from rest_framework import serializers

from car.models import CarBrand, CarModel, CarOption, FuelType, CarTransmission, CarImage, Car


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Car model name must be at least 2 characters long")
        return value


class CarOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOption
        fields = '__all__'

    def validate_option_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Option name must be at least 3 characters long.")
        return value


class FuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = '__all__'

    def validate_name(self, value):
        if value in ["Petrol", "Diesel", "Gasoline", "Hybrid", "Electric"]:
            return value
        raise serializers.ValidationError \
            ("Invalid fuel type name.Valid fuel types are Petrol, Diesel, Gasoline, Hybrid,Electric")


class CarTransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTransmission
        fields = '__all__'

    def validate_name(self, value):
        if value not in ['Manual', 'Automatic']:
            raise serializers.ValidationError("Transmission type must be either 'Manual' or 'Automatic'.")
        return value


class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = '__all__'

    def validate_image(self, value):
        if value.size > (1024 * 1024):
            raise serializers.ValidationError("Image size should be less than 1 MB")
        return value


class CarSerializer(serializers.ModelSerializer):

    def validate_fuel_type(self, value):
        if not FuelType.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("This fuel type does not exist.")
        return value

    def validate_transmission(self, value):
        if not CarTransmission.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("This transmission does not exist.")
        return value

    class Meta:
        model = Car
        fields = '__all__'
