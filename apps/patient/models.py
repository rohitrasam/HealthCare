from django.db import models

# Create your models here.

class Patient(models.Model):

    class Gender(models.TextChoices):
        MALE = "M"
        FEMALE = "F"
        NOT_SPECIFIED = "NA"

    name = models.CharField(max_length=60)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.NOT_SPECIFIED)
    contact_no = models.CharField(max_length=10, unique=True)
    address = models.CharField(max_length=80)
    email = models.EmailField(max_length=30, unique=True)