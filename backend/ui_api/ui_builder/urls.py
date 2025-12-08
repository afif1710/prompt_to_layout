from django.urls import path
from . import views

urlpatterns = [
    path("generate-ui", views.generate_ui, name="generate-ui"),
    path("upload-sketch", views.upload_sketch, name="upload-sketch"),
    path("projects", views.list_projects, name="list-projects"),
    path("save-project", views.save_project, name="save-project"),
    path("download-zip", views.download_zip, name="download-zip"),
]
