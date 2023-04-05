from django.db import models

# Create your models here.

class Patients(models.Model):
    secret_id = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)