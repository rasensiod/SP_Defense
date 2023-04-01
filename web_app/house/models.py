from django.db import models

# Create your models here.

class Devices(models.Model):
    maker = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)