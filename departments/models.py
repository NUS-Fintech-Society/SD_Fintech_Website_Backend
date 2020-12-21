from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    icon = models.CharField(default='', max_length=1000)
    route = models.CharField(default='', max_length=1000)
    purpose = models.TextField(default='')
    goal = models.TextField(default='')

    def __str__(self):
        return self.name