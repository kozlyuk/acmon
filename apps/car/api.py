from rest_framework import viewsets, permissions

from . import serializers
from . import models


class BrandViewSet(viewsets.ModelViewSet):
    """ViewSet for the Brand class"""

    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarViewSet(viewsets.ModelViewSet):
    """ViewSet for the Car class"""

    queryset = models.Car.objects.all()
    serializer_class = serializers.CarSerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for the Company class"""

    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartmentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Department class"""

    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ModelViewSet(viewsets.ModelViewSet):
    """ViewSet for the Model class"""

    queryset = models.Model.objects.all()
    serializer_class = serializers.ModelSerializer
    permission_classes = [permissions.IsAuthenticated]
