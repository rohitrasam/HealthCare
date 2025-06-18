from rest_framework import serializers as sz
from .models import Patient

class PatientSerializer(sz.ModelSerializer):

    class Meta:
        model = Patient
        fields = "__all__"
    