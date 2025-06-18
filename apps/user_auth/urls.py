from django.urls import path
from .views import *

urlpatterns = [
    path('register', view=UserRegisterView.as_view()),
    path('login', view=UserLoginView.as_view()),
]