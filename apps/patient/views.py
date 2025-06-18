from .models import Patient
from .serializers import PatientSerializer
from ..base import views
# Create your views here.


class PatientListCreateView(views.BaseListCreateView):
    
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    model_name = "Patient"


class PatientDetailsView(views.BaseDetailsView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    model_name = "Patient"