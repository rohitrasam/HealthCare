from .models import Patient
from .serializers import PatientSerializer
from ..base import views
# Create your views here.


class PatientListCreateView(views.BaseListCreateView):
    
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    model_name = "Patient"

    # def get(self, request: Request) -> Response:
    #     query_set = self.get_queryset()
    #     serializer = PatientSerializer(query_set, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request: Request) -> Response:

    #     serializer = self.get_serializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"message": "Patient added successfully!"}, status=status.HTTP_201_CREATED)

    #     return Response(
    #         {
    #             "message": "Failed to add patient.", 
    #             "errors": serializer.errors
    #         }, 
    #         status=status.HTTP_400_BAD_REQUEST
    #     )


class PatientDetailsView(views.BaseDetailsView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    model_name = "Patient"

    # def get(self, request: Request, *args, **kwargs) -> Response:
        
    #     try:
    #         patient: Patient = self.get_object()
    #         serializer: PatientSerializer = self.get_serializer(patient)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except:
    #         return Response({"message": "Could not find patient."}, status=status.HTTP_404_NOT_FOUND)
            
    # def put(self, request: Request, *args, **kwargs) -> Response:

    #     patient: Patient = self.get_object()
    #     data = request.data
    #     serializer: PatientSerializer = self.get_serializer(patient, data=data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"message": "Patient details updated."}, status=status.HTTP_200_OK)
        
    #     return Response(
    #         {
    #             "message": "Failed to update details",
    #             "error": serializer.errors        
    #         }, status=status.HTTP_400_BAD_REQUEST
    #     )

    # def delete(self, request: Request, *args, **kwargs) -> Response:
    #     try:
    #         patient: Patient = self.get_object()
    #         patient.delete()
    #         return Response({"message": "Patient details deleted."}, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return Response({"message": "Could not find patient."}, status=status.HTTP_200_OK)
