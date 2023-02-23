from django.contrib import admin
from car.models import Car, CarModel, FuelType, CarOption, CarTransmission,CarBrand, CarImage

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["brand","car_model","year", "color", "cost_per_day", "transmission","is_available","is_employer","fueltype"]



@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(CarOption)
class CarOptionAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(CarImage)
class CarImagedAdmin(admin.ModelAdmin):
    list_display = ["car"]

@admin.register(CarTransmission)
class CarTransmissionAdmin(admin.ModelAdmin):
    list_display = ["name"]
