from django.db import models

class Project(models.Model):
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    files = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.project_name
