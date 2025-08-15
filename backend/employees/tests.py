from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


# Create your tests here.


class EmployeeApiTests(APITestCase):
	def setUp(self):
		self.admin = User.objects.create_user(email='admin@example.com', password='adminpass', role='ADMIN')
		self.client_user = User.objects.create_user(email='clientuser@example.com', password='clientpass', role='CLIENT')

	def auth(self, email, password):
		res = self.client.post('/api/auth/login/', {"email": email, "password": password}, format='json')
		self.assertEqual(res.status_code, status.HTTP_200_OK)
		self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {res.data['data']['access_token']}")

	def test_client_can_list_employees(self):
		self.auth('clientuser@example.com', 'clientpass')
		res = self.client.get('/api/employees/')
		self.assertEqual(res.status_code, status.HTTP_200_OK)

	def test_client_cannot_create_employee(self):
		self.auth('clientuser@example.com', 'clientpass')
		payload = {
			"first_name": "Jane",
			"last_name": "Doe",
			"email": "jane@acme.com",
			"phone": "1234567890",
			"position": "Engineer",
			"department": "Dev",
			"salary_per_month": "5000.00",
			"start_date": "2024-01-01",
			"skills": "Python",
			"description": "Backend dev"
		}
		res = self.client.post('/api/employees/', payload, format='json')
		self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
