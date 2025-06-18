from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.db.models import QuerySet
from ..patient.models import Patient
from ..doctor.models import Doctor
from ..patient.serializers import PatientSerializer
from ..doctor.serializers import DoctorSerializer

# Create your views here.


class BaseListCreateView(generics.ListCreateAPIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        query_set: QuerySet[Patient | Doctor] = self.get_queryset()
        serializer: PatientSerializer | DoctorSerializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:

        serializer: PatientSerializer | DoctorSerializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"{self.model_name} added successfully!"}, status=status.HTTP_201_CREATED)

        return Response(
            {
                "message": f"Failed to add {self.model_name.lower()}.", 
                "errors": serializer.errors
            }, 
            status=status.HTTP_400_BAD_REQUEST
        )


class BaseDetailsView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get(self, request: Request, *args, **kwargs) -> Response:
        
        try:
            instance: Patient | Doctor = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message": f"Could not find {self.model_name.lower()}."}, status=status.HTTP_404_NOT_FOUND)
            
    def put(self, request: Request, *args, **kwargs) -> Response:

        instance: Patient | Doctor = self.get_object()
        data = request.data
        serializer: PatientSerializer | DoctorSerializer = self.get_serializer(instance, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": f"{self.model_name} details updated."}, status=status.HTTP_200_OK)
        
        return Response(
            {
                "message": "Failed to update details",
                "error": serializer.errors        
            }, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request: Request, *args, **kwargs) -> Response:
        try:
            instance: Patient | Doctor = self.get_object()
            instance.delete()
            return Response({"message": f"{self.model_name} details deleted."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": f"Could not find {self.model_name.lower()}."}, status=status.HTTP_200_OK)
