from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin
from .models import Client
from .serializers import ClientSerializer


# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
	queryset = Client.objects.all().order_by('-created_at')
	serializer_class = ClientSerializer
	permission_classes = [IsAuthenticated]
	filterset_fields = ["status", "industry", "joining_date"]
	search_fields = ["company", "contact_name", "email", "industry"]
	ordering_fields = ["company", "joining_date", "status"]

	def get_permissions(self):
		if self.request.method in ("POST", "PUT", "PATCH", "DELETE"):
			return [IsAdmin()]
		return super().get_permissions()

	def list(self, request, *args, **kwargs):
		response = super().list(request, *args, **kwargs)
		return Response({"success": True, "message": "Clients fetched", "data": response.data}, status=200)

	def retrieve(self, request, *args, **kwargs):
		response = super().retrieve(request, *args, **kwargs)
		return Response({"success": True, "message": "Client fetched", "data": response.data}, status=200)

	def create(self, request, *args, **kwargs):
		response = super().create(request, *args, **kwargs)
		return Response({"success": True, "message": "Client created", "data": response.data}, status=response.status_code)

	def update(self, request, *args, **kwargs):
		response = super().update(request, *args, **kwargs)
		return Response({"success": True, "message": "Client updated", "data": response.data}, status=response.status_code)

	def destroy(self, request, *args, **kwargs):
		response = super().destroy(request, *args, **kwargs)
		if response.status_code == 204:
			return Response({"success": True, "message": "Client deleted", "data": None}, status=200)
		return Response({"success": False, "message": "Delete failed", "data": None}, status=response.status_code)
