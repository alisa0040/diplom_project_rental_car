from django.contrib import admin

from reservation.models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["customer", "car","start_date","end_date"]
