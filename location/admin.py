from django.contrib import admin
from location.models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["city","address"]
