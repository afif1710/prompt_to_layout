from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "project_name", "created_at")
    search_fields = ("project_name", "description")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)
