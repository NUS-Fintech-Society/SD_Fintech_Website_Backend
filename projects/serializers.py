from rest_framework import serializers
from .models import Project, ProjectImageUrl


class ProjectImageUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImageUrl
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    imageUrls = ProjectImageUrlSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
