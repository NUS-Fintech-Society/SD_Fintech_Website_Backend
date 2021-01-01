from django.db import models
from departments.models import Department
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ProjectImageUrl(models.Model):
    url = models.URLField
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
