from typing import Dict
from rest_framework import serializers as sz
from .models import User

class UserRegisterSerializer(sz.ModelSerializer):

    class Meta:
        model = User
        fields = ["email", "name", "password"]
        extra_kwargs = {
                "password": {"write_only": True},
                "name": {"read_only":True}
            }
    
    def create(self, validated_data: Dict[str, str]) -> User:
        user = self.Meta.model.objects.create_user(**validated_data)
        return user if user else None


class UserLoginSerializer(sz.Serializer):

    email = sz.EmailField()
    password = sz.CharField(write_only=True)