# user-service/users/views.py
from rest_framework import viewsets
from .models import HealthcareProfessional
from .serializers import HealthcareProfessionalSerializer


class HealthcareProfessionalViewSet(viewsets.ModelViewSet):
    queryset = HealthcareProfessional.objects.all()
    serializer_class = HealthcareProfessionalSerializer
