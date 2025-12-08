from rest_framework import serializers
from .models import Project

class GenerateUIRequestSerializer(serializers.Serializer):
    description = serializers.CharField()
    theme = serializers.CharField(required=False, default="minimal-light")
    complexity = serializers.IntegerField(required=False, min_value=1, max_value=5, default=3)

class UploadSketchSerializer(serializers.Serializer):
    file = serializers.ImageField()
    theme = serializers.CharField(required=False, default="minimal-light")
    complexity = serializers.IntegerField(required=False, min_value=1, max_value=5, default=3)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "project_name", "description", "files", "created_at"]

class SaveProjectSerializer(serializers.Serializer):
    project_name = serializers.CharField()
    description = serializers.CharField()
    files = serializers.JSONField()
