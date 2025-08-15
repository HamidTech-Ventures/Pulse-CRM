from django.db import models


class Project(models.Model):
	class Priority(models.TextChoices):
		LOW = 'Low', 'Low'
		MEDIUM = 'Medium', 'Medium'
		HIGH = 'High', 'High'

	project_name = models.CharField(max_length=255)
	client = models.ForeignKey('clients.Client', on_delete=models.CASCADE, related_name='projects')
	description = models.TextField(blank=True)
	budget = models.DecimalField(max_digits=12, decimal_places=2)
	priority = models.CharField(max_length=10, choices=Priority.choices)
	deadline = models.DateField()
	team = models.ManyToManyField('employees.Employee', related_name='projects', blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.project_name
