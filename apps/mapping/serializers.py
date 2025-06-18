import rest_framework.serializers as sz

from ..doctor.models import Doctor
from ..patient.models import Patient
from ..doctor.serializers import DoctorSerializer
from ..patient.serializers import PatientSerializer
from .models import Mapping

class MappingSerializer(sz.ModelSerializer):

    patient_id = sz.PrimaryKeyRelatedField(queryset=Patient.objects.all(), source="patient", write_only=True)
    doctor_id = sz.PrimaryKeyRelatedField(queryset=Doctor.objects.all(), source="doctor", write_only=True)

    patient = sz.CharField(source="patient.name", read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = Mapping
        fields = ["patient", "doctor","patient_id", "doctor_id"]





    