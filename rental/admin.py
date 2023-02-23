from django.contrib import admin

from rental.models import Rental


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ["customer", "car","start_date","end_date"]
