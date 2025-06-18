from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer
from .models import User
from  rest_framework_simplejwt.tokens import AccessToken
# Create your views here.


class UserRegisterView(CreateAPIView):

    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Registered Successfully!", status=status.HTTP_201_CREATED)

    
        return Response(
                    {
                        "message": "Couldn't register. Try again! Could be one of the reasons below:", 
                        "errors": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
            )

    
class UserLoginView(APIView):

    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request: Request) -> Response:

        data = request.data
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response(
                {
                    "message":" Failed to login! Try again", 
                    "errors": serializer.errors
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        user: User = authenticate(email=email, password=password)
        if not user:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        access_token = AccessToken.for_user(user)
        return Response({"access": f"Bearer {str(access_token)}"}, status=status.HTTP_200_OK)