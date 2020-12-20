from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    #icon = models.
    #route = models.