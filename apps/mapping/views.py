from rest_framework.request import Request
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated

from ..doctor.serializers import DoctorSerializer
from .models import Mapping
from ..patient.models import Patient
from .serializers import MappingSerializer
# Create your views here.

class ListCreateMappingView(generics.ListCreateAPIView):

    queryset = Mapping.objects.select_related()
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        data = request.data

        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response("Mapped successfully!", status=status.HTTP_200_OK)

        return Response({
                        "message": "Could not map patient and doctor!", 
                        "errors": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

    def get(self, request: Request) -> Response:

        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    

class MappingDetailView(generics.ListAPIView):

    queryset = Patient.objects.prefetch_related("doctor")
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, *args, **kwargs) -> Response:
        patient_id = kwargs['patient_id']
        queryset = self.get_queryset()
        filtered = queryset.filter(id=patient_id)
        if filtered.exists():
            instance = filtered.first()
            serializer = self.get_serializer(instance.doctor.all(), many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response({"message": f"No patient with id {patient_id} exists."}, status=status.HTTP_404_NOT_FOUND)


class MappingDeleteView(generics.DestroyAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Mapping.objects.all()
    lookup_url_kwarg = 'id'

    def delete(self, request: Request, *args, **kwargs) -> Response:
        try:
            mapping = self.get_object()
            mapping.delete()
            return Response({"message": "Mapping deleted successfully!"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Requested doctor-patient mapping does not exist"}, status=status.HTTP_404_NOT_FOUND)