from django.urls import path
from .views import *

urlpatterns = [
    
    path('', view=ListCreateMappingView.as_view()),
    path('<int:patient_id>', MappingDetailView.as_view(), name="patient-mapping-list"),
    path('delete/<int:id>', MappingDeleteView.as_view(), name="delete-mapping"),
]