from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ("project_name", "client", "priority", "deadline", "budget")
	search_fields = ("project_name", "client__company")
	list_filter = ("priority", "deadline")
