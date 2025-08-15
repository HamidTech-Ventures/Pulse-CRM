from django.db import models


class Client(models.Model):
	class Status(models.TextChoices):
		ACTIVE = 'Active', 'Active'
		COMPLETE = 'Complete', 'Complete'
		PROSPECTS = 'Prospects', 'Prospects'

	contact_name = models.CharField(max_length=255)
	company = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=50)
	industry = models.CharField(max_length=255)
	website = models.URLField(blank=True)
	address = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	status = models.CharField(max_length=20, choices=Status.choices)
	joining_date = models.DateField()

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.company} ({self.status})"
