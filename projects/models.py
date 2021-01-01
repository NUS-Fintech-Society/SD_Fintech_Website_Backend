from django.db import models
from departments.models import Department
# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return '[' + self.department.name + '] ' + self.title


class ProjectImageUrl(models.Model):
    url = models.URLField(max_length=200, default='')
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='imageUrls')

    def __str__(self):
        return '[' + self.project.department.name + '] ' + self.project.title + ' ' + str(self.id)
