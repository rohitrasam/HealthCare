from .models import Doctor
from .serializers import DoctorSerializer
from ..base import views


class DoctorListCreateView(views.BaseListCreateView):
    
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    model_name = "Doctor"


class DoctorDetailsView(views.BaseDetailsView):

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    model_name = "Doctor"