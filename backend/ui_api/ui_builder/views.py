from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .serializers import (
    GenerateUIRequestSerializer,
    UploadSketchSerializer,
    ProjectSerializer,
    SaveProjectSerializer,
)
from .models import Project
from .ai import generate_from_description, generate_from_sketch
from .utils.zip_utils import create_zip_from_files
from .utils.jsx_validator import validate_jsx_stub

@api_view(["POST"])
def generate_ui(request):
    """Generate UI from natural language description"""
    serializer = GenerateUIRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    try:
        result = generate_from_description(
            data["description"], 
            data.get("theme", "minimal-light"), 
            data.get("complexity", 3)
        )

        if not validate_jsx_stub(result["files"]):
            return Response(
                {"detail": "Generated code failed validation."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response(result)
    except Exception as e:
        return Response(
            {"detail": f"Error generating UI: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["POST"])
def upload_sketch(request):
    """Generate UI from uploaded sketch"""
    serializer = UploadSketchSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    try:
        result = generate_from_sketch(
            data["file"], 
            data.get("theme", "minimal-light"), 
            data.get("complexity", 3)
        )

        if not validate_jsx_stub(result["files"]):
            return Response(
                {"detail": "Generated code failed validation."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response(result)
    except Exception as e:
        return Response(
            {"detail": f"Error processing sketch: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["GET"])
def list_projects(request):
    """List all saved projects"""
    projects = Project.objects.all()[:30]
    return Response(ProjectSerializer(projects, many=True).data)

@api_view(["POST"])
def save_project(request):
    """Save a generated project"""
    serializer = SaveProjectSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        project = Project.objects.create(**serializer.validated_data)
        return Response(
            ProjectSerializer(project).data, 
            status=status.HTTP_201_CREATED
        )
    except Exception as e:
        return Response(
            {"detail": f"Error saving project: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["POST"])
def download_zip(request):
    """Download project files as ZIP"""
    files = request.data.get("files", {})

    if not isinstance(files, dict):
        return Response(
            {"detail": "files must be an object."},
            status=status.HTTP_400_BAD_REQUEST
        )

    if not files:
        return Response(
            {"detail": "No files provided."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        zip_bytes = create_zip_from_files(files)
        resp = HttpResponse(zip_bytes, content_type="application/zip")
        resp["Content-Disposition"] = 'attachment; filename="ui-project.zip"'
        return resp
    except Exception as e:
        return Response(
            {"detail": f"Error creating ZIP: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
