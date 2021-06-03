from rest_framework import viewsets, permissions

from . import serializers
from . import models


class TripViewSet(viewsets.ModelViewSet):
    """ViewSet for the Trip class"""

    queryset = models.Trip.objects.all()
    serializer_class = serializers.TripSerializer
    permission_classes = [permissions.IsAuthenticated]


class RecordViewSet(viewsets.ModelViewSet):
    """ViewSet for the Record class"""

    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordSerializer
    permission_classes = [permissions.IsAuthenticated]
