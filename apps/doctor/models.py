from django.db import models

# Create your models here.

class Doctor(models.Model):

    name = models.CharField(max_length=60)
    specialization = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=30, unique=True)

