from django.db import models


class Employee(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=50)
	position = models.CharField(max_length=255)
	department = models.CharField(max_length=255)
	salary_per_month = models.DecimalField(max_digits=10, decimal_places=2)
	start_date = models.DateField()
	skills = models.TextField(blank=True)
	description = models.TextField(blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"
