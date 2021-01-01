from rest_framework import serializers
from .models import Project, ProjectImageUrl


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectImageUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImageUrl
        fields = '__all__'
