from datetime import datetime
from rest_framework import viewsets, permissions, pagination

from . import serializers
from . import models


class TripViewSet(viewsets.ModelViewSet):
    """ViewSet for the Trip class"""

    queryset = models.Trip.objects.all()
    serializer_class = serializers.TripSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # get filtered payments
        queryset = models.Trip.objects.all()
        # get parameters from request
        car_ids = self.request.GET.getlist('car_id')
        from_date = self.request.query_params.get('from_date')
        end_date = self.request.query_params.get('end_date')
        order = self.request.GET.get('order')
        # filtering queryset
        if car_ids:
            qs_union = models.Trip.objects.none()
            for car in car_ids:
                qs_segment = queryset.filter(car=car)
                qs_union = qs_union | qs_segment
            queryset = qs_union
        if from_date:
            queryset = queryset.filter(start_time__gte=from_date)
        if end_date:
            queryset = queryset.filter(start_time__lte=end_date)

        # ordering queryset
        if order:
            queryset = queryset.order_by(order)
        else:
            queryset = queryset.order_by('-start_time')

        return queryset


class RecordViewSet(viewsets.ModelViewSet):
    """ViewSet for the Record class
    Filter queryset by car_id field ('car_id' get parameters list)
    Filter queryset by start_time field ('start_time' get parameter)
    Filter queryset by end_time field ('end_time' get parameter)
    Order queryset by any given field ('order' get parameter)
    """
    serializer_class = serializers.RecordSerializer
    permission_classes = [permissions.IsAuthenticated]
    viewsets.ModelViewSet.pagination_class.default_limit = 10000

    def get_queryset(self):
        # get filtered payments
        queryset = models.Record.objects.all()
        # get parameters from request
        car_ids = self.request.GET.getlist('car_id')
        start_time = self.request.query_params.get('start_time',
            datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
        end_time = self.request.query_params.get('end_time', datetime.now())
        order = self.request.GET.get('order')
        events = self.request.GET.get('events')
        # filtering queryset
        if car_ids:
            qs_union = models.Record.objects.none()
            for car in car_ids:
                qs_segment = queryset.filter(car=car)
                qs_union = qs_union | qs_segment
            queryset = qs_union
        queryset = queryset.filter(timestamp__gte=start_time,
                                   timestamp__lte=end_time)
        if events in ['1', 'true']:
            queryset = queryset.exclude(event_id=0)
        else:
            queryset = queryset.filter(event_id=0)
        # ordering queryset
        if order:
            queryset = queryset.order_by(order)
        else:
            queryset = queryset.order_by('timestamp')

        return queryset
