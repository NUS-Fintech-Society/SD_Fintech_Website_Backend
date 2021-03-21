from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

# Create your views here.
from .serializers import ProjectSerializer
from .models import Project

class ProjectListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailsView(APIView):

    def get_object(self, id):
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        project = self.get_object(id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


class DepartmentProjects(APIView):

    def get(self, request, id):
        projects = Project.objects.filter(department=id)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
