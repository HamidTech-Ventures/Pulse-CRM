from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin
from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-created_at')
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["department", "start_date"]
    search_fields = ["first_name", "last_name", "email", "position", "department"]
    ordering_fields = ["first_name", "last_name", "start_date"]

    def get_permissions(self):
        if self.request.method in ("POST", "PUT", "PATCH", "DELETE"):
            return [IsAdmin()]
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({"success": True, "message": "Employees fetched", "data": response.data}, status=200)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response({"success": True, "message": "Employee fetched", "data": response.data}, status=200)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"success": True, "message": "Employee created", "data": response.data}, status=response.status_code)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({"success": True, "message": "Employee updated", "data": response.data}, status=response.status_code)

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == 204:
            return Response({"success": True, "message": "Employee deleted", "data": None}, status=200)
        return Response({"success": False, "message": "Delete failed", "data": None}, status=response.status_code)
