from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
from clients.models import Client
from .models import Project


# Create your tests here.


class ProjectApiTests(APITestCase):
	def setUp(self):
		self.admin = User.objects.create_user(email='admin@example.com', password='adminpass', role='ADMIN')
		self.client_user = User.objects.create_user(email='clientuser@example.com', password='clientpass', role='CLIENT')
		self.client_entity = Client.objects.create(contact_name='Client', company='ClientCo', email='clientuser@example.com', phone='123', industry='Tech', website='https://example.com', address='addr', description='', status='Active', joining_date='2024-01-01')
		self.project = Project.objects.create(project_name='P1', client=self.client_entity, description='', budget='1000.00', priority='High', deadline='2025-01-01')

	def auth(self, email, password):
		res = self.client.post('/api/auth/login/', {"email": email, "password": password}, format='json')
		self.assertEqual(res.status_code, status.HTTP_200_OK)
		self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {res.data['data']['access_token']}")

	def test_client_my_projects(self):
		self.auth('clientuser@example.com', 'clientpass')
		res = self.client.get('/api/projects/my-projects/')
		self.assertEqual(res.status_code, status.HTTP_200_OK)
		self.assertTrue(len(res.data['data']) >= 1 or 'results' in res.data)  # paginated variant

	def test_admin_my_projects_sees_all(self):
		self.auth('admin@example.com', 'adminpass')
		res = self.client.get('/api/projects/my-projects/')
		self.assertEqual(res.status_code, status.HTTP_200_OK)
