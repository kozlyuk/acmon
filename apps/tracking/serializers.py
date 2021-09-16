from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin

from . import models
from apps.devices.models import Parameter


class TripSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    trip_time = serializers.SerializerMethodField()

    class Meta:
        model = models.Trip
        fields = [
            "id",
            "name",
            "car",
            # "driver",
            "distance",
            "start_time",
            "finish_time",
            "trip_time",
            "updated_at",
            "created_at",
        ]

    def get_trip_time(self, obj):

        return obj.trip_time()


class RecordSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    io_elements = serializers.SerializerMethodField()
    event = serializers.SerializerMethodField()

    class Meta:
        model = models.Record
        fields = [
            "id",
            "car",
            "timestamp",
            "priority",
            "longitude",
            "latitude",
            "altitude",
            "angle",
            "satellites",
            "speed",
            "event",
            "io_elements",
            "is_parked",
        ]

    def get_io_elements(self, obj):
        params = []
        if obj.io_elements:
            param_names = Parameter.objects.filter(code__in=obj.io_elements.keys()) \
                                           .values('code', 'name', 'units', 'multiplier')
            for parameter in param_names:
                if parameter['multiplier']:
                    value = obj.io_elements[(str(parameter['code']))] * parameter['multiplier']
                else:
                    value = obj.io_elements[(str(parameter['code']))]
                params.append({'code': parameter['code'],
                               'name': parameter['name'],
                               'value': value,
                               'units': parameter['units']
                               })
        return params

    def get_event(self, obj):

        if obj.event_id:
            parameter = Parameter.objects.get(code=obj.event_id)
            if parameter.multiplier:
                value = obj.io_elements[(str(parameter.code))] * parameter.multiplier
            else:
                value = obj.io_elements[(str(parameter.code))]

            return {'code': parameter.code,
                    'name': parameter.name,
                    'value': value,
                    'units': parameter.units
                    }
