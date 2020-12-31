from rest_framework import serializers
from .models import Project, ProjectImageUrls


class ProjectSerializer(serializers.ProjectSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectImageUrlSerializer(serializers.ProjectImageUrlSerializer):
    class Meta:
        model = ProjectImageUrls
        fields = '__all__'
