from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=50)
    details = models.TextField()

    def __str__(self):
        return self.title


class ProjectImageUrls(models.Model):
    url = models.URLField
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
