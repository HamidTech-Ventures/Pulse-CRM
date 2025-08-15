from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ("first_name", "last_name", "email", "position", "department", "start_date")
	search_fields = ("first_name", "last_name", "email", "position", "department")
	list_filter = ("department", "start_date")
