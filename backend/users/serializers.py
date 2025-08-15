from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'email', 'role', 'is_active']


class LoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField(write_only=True)

	def validate(self, attrs):
		email = attrs.get('email')
		password = attrs.get('password')
		user = authenticate(request=self.context.get('request'), email=email, password=password)
		if not user:
			raise serializers.ValidationError('Invalid email or password')
		attrs['user'] = user
		return attrs