from django.db import models

# Create your models here.
class Event(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=100)
  description = models.CharField(max_length=1000)
  start = models.DateTimeField(auto_now=False, auto_now_add=False)
  end = models.DateTimeField(auto_now=False, auto_now_add=False)

  def __str__(self):
    return self.name
