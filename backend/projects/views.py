from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdmin
from .models import Project
from .serializers import ProjectSerializer


# Create your views here.

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["priority", "client", "deadline"]
    search_fields = ["project_name", "client__company", "description"]
    ordering_fields = ["project_name", "deadline", "priority", "budget"]

    def get_queryset(self):
        base_qs = Project.objects.select_related('client').prefetch_related('team').all().order_by('-created_at')
        user = self.request.user
        if getattr(user, 'role', None) == 'CLIENT':
            from clients.models import Client
            try:
                client = Client.objects.get(email=user.email)
            except Client.DoesNotExist:
                return base_qs.none()
            return base_qs.filter(client=client)
        return base_qs

    def get_permissions(self):
        if self.request.method in ("POST", "PUT", "PATCH", "DELETE"):
            return [IsAdmin()]
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({"success": True, "message": "Projects fetched", "data": response.data}, status=200)

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response({"success": True, "message": "Project fetched", "data": response.data}, status=200)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"success": True, "message": "Project created", "data": response.data}, status=response.status_code)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({"success": True, "message": "Project updated", "data": response.data}, status=response.status_code)

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        if response.status_code == status.HTTP_204_NO_CONTENT:
            return Response({"success": True, "message": "Project deleted", "data": None}, status=200)
        return Response({"success": False, "message": "Delete failed", "data": None}, status=response.status_code)

    @action(detail=False, methods=['get'], url_path='my-projects', permission_classes=[IsAuthenticated])
    def my_projects(self, request):
        user = request.user
        if getattr(user, 'role', None) == 'CLIENT':
            from clients.models import Client
            try:
                client = Client.objects.get(email=user.email)
            except Client.DoesNotExist:
                return Response({"success": True, "message": "No projects", "data": []}, status=200)
            qs = self.get_queryset().filter(client=client)
        else:
            qs = self.get_queryset()
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            paginated = self.get_paginated_response(serializer.data)
            return Response({"success": True, "message": "My projects", "data": paginated.data}, status=200)
        serializer = self.get_serializer(qs, many=True)
        return Response({"success": True, "message": "My projects", "data": serializer.data}, status=200)
