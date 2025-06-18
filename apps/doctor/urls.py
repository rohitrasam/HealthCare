from django.urls import path
from .views import *

urlpatterns = [
    
    path('', view=DoctorListCreateView.as_view()),
    path('<int:id>', view=DoctorDetailsView.as_view()),
]