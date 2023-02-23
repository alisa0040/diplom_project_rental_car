from django.contrib import admin

from employer.models import Employer


@admin.register(Employer)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name","phone", "address"]
