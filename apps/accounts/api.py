from rest_framework import viewsets, permissions

from . import serializers
from . import models



class ContactViewSet(viewsets.ModelViewSet):
    """ViewSet for the Contact class"""

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# class OperatorViewSet(viewsets.ModelViewSet):
#     """ViewSet for the Operator class"""

#     queryset = models.Operator.objects.all()
#     serializer_class = serializers.OperatorSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class DriverViewSet(viewsets.ModelViewSet):
#     """ViewSet for the Driver class"""

#     queryset = models.Driver.objects.all()
#     serializer_class = serializers.DriverSerializer
#     permission_classes = [permissions.IsAuthenticated]
