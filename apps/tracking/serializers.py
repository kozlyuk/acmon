from rest_framework import serializers

from drf_dynamic_fields import DynamicFieldsMixin

from . import models


class TripSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = models.Trip
        fields = [
            "id",
            "car",
            "driver",
            "start_time",
            "finsh_time",
            "updated_at",
            "created_at",
        ]


class RecordSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

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
            "updated_at",
            "created_at",
            "event_id",
            "io_elements"
        ]
