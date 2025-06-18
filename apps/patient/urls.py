from django.urls import path
from .views import *

urlpatterns = [
    
    path('', view=PatientListCreateView.as_view()),
    path('<int:id>', view=PatientDetailsView.as_view()),
]