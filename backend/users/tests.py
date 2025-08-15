from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

# Create your tests here.


class AuthTests(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(email='user@example.com', password='testpass', role='CLIENT')

	def test_login_returns_token_and_role(self):
		res = self.client.post('/api/auth/login/', {"email": "user@example.com", "password": "testpass"}, format='json')
		self.assertEqual(res.status_code, status.HTTP_200_OK)
		self.assertTrue(res.data['success'])
		self.assertIn('access_token', res.data['data'])
		self.assertEqual(res.data['data']['role'], 'CLIENT')
