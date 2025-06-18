from typing import Dict
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email: str, password: str, **valdidated_data: Dict[str, str]) -> "User":
        if not email:
            raise ValueError("Email required.")
        if not password:
            raise ValueError("Password required.")
        
        email = self.normalize_email(email)
        user: User = self.model(**valdidated_data, email=email)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):

    email = models.EmailField(max_length=60, unique=True)
    name = models.CharField(max_length=40, unique=True)
    objects = UserManager()

    USERNAME_FIELD = "email"