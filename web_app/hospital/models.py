from django.db import models

# Create your models here.

class Patients(models.Model):
    secret_id = models.IntegerField()
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    medication = models.CharField(max_length=100)