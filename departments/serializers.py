from rest_framework import serializers
from .models import Department
from projects.serializers import ProjectSerializer


class DepartmentSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = '__all__'
