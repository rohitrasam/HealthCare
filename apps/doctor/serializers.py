from rest_framework import serializers as sz
from .models import Doctor

class DoctorSerializer(sz.ModelSerializer):

    class Meta:
        model = Doctor
        fields = "__all__"
    