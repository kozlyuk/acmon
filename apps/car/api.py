from rest_framework import viewsets, permissions

from . import serializers
from . import models


class BrandViewSet(viewsets.ModelViewSet):
    """ViewSet for the Brand class"""

    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    permission_classes = [permissions.IsAuthenticated]


class CarViewSet(viewsets.ModelViewSet):
    """ViewSet for the Car class
    Filter queryset by car_id field ('car_id' get parameters list)
    Order queryset by any given field ('order' get parameter)
    """
    serializer_class = serializers.CarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # get filtered payments
        queryset = models.Car.objects.all()
        # get parameters from request
        car_ids = self.request.GET.getlist('car_id')
        order = self.request.GET.get('order')
        # filtering queryset
        if car_ids:
            qs_union = models.Car.objects.none()
            for car in car_ids:
                qs_segment = queryset.filter(id=car)
                qs_union = qs_union | qs_segment
            queryset = qs_union
        # ordering queryset
        if order:
            queryset = queryset.order_by(order)

        return queryset


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
