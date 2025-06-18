from django.db import models

# Create your models here.

class Mapping(models.Model):

    doctor = models.ForeignKey("doctor.Doctor", related_name="patient", on_delete=models.CASCADE)
    patient = models.ForeignKey("patient.Patient", related_name="doctor", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('patient', 'doctor')