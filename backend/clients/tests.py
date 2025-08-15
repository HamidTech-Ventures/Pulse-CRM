from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from .models import Client


class ClientApiTests(APITestCase):
	def setUp(self):
		self.admin = User.objects.create_user(email='admin@example.com', password='adminpass', role='ADMIN')
		self.client_user = User.objects.create_user(email='clientuser@example.com', password='clientpass', role='CLIENT')

	def auth(self, user):
		url = reverse('auth-login')
		res = self.client.post('/api/auth/login/', {"email": user.email, "password": "adminpass" if user.role=='ADMIN' else 'clientpass'}, format='json')
		self.assertEqual(res.status_code, status.HTTP_200_OK)
		token = res.data['data']['access_token']
		self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

	def test_admin_can_create_client(self):
		self.auth(self.admin)
		payload = {
			"contact_name": "John Doe",
			"company": "Acme Inc",
			"email": "client@acme.com",
			"phone": "1234567890",
			"industry": "Tech",
			"website": "https://acme.com",
			"address": "123 Street",
			"description": "Important client",
			"status": "Active",
			"joining_date": "2024-01-01"
		}
		res = self.client.post('/api/clients/', payload, format='json')
		self.assertEqual(res.status_code, status.HTTP_201_CREATED)

	def test_client_cannot_create_client(self):
		self.auth(self.client_user)
		payload = {
			"contact_name": "John Doe",
			"company": "Acme Inc",
			"email": "client2@acme.com",
			"phone": "1234567890",
			"industry": "Tech",
			"website": "https://acme.com",
			"address": "123 Street",
			"description": "Important client",
			"status": "Active",
			"joining_date": "2024-01-01"
		}
		res = self.client.post('/api/clients/', payload, format='json')
		self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
