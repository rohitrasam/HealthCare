from .models import Doctor
from .serializers import DoctorSerializer
from ..base import views
# Create your views here.


class DoctorListCreateView(views.BaseListCreateView):
    
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    model_name = "Doctor"

    # def get(self, request: Request) -> Response:
    #     query_set = self.get_queryset()
    #     serializer = DoctorSerializer(query_set, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request: Request) -> Response:

    #     serializer = self.get_serializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"message": "Doctor added successfully!"}, status=status.HTTP_201_CREATED)

    #     return Response(
    #         {
    #             "message": "Failed to add doctor.", 
    #             "errors": serializer.errors
    #         }, 
    #         status=status.HTTP_400_BAD_REQUEST
    #     )


class DoctorDetailsView(views.BaseDetailsView):

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    model_name = "Doctor"

    # def get(self, request: Request, *args, **kwargs) -> Response:
        
    #     try:
    #         doctor: Doctor = self.get_object()
    #         serializer: DoctorSerializer = self.get_serializer(doctor)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except:
    #         return Response({"message": "Could not find doctor."}, status=status.HTTP_404_NOT_FOUND)
            
    # def put(self, request: Request, *args, **kwargs) -> Response:
    #     try:
    #         doctor: Doctor = self.get_object()
    #         data = request.data
    #         serializer: DoctorSerializer = self.get_serializer(doctor, data=data)

    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response({"message": "Doctor details updated."}, status=status.HTTP_200_OK)
            
    #         return Response(
    #             {
    #                 "message": "Failed to update details",
    #                 "error": serializer.errors        
    #             }, status=status.HTTP_400_BAD_REQUEST
    #         )
    #     except Exception as e:
    #         return Response({"message": "Could not find doctor."}, status=status.HTTP_404_NOT_FOUND)

    # def delete(self, request: Request, *args, **kwargs) -> Response:
    #     try:
    #         doctor: Doctor = self.get_object()
    #         doctor.delete()
    #         return Response({"message": "Doctor details deleted."}, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return Response({"message": "Could not find doctor."}, status=status.HTTP_404_NOT_FOUND)

