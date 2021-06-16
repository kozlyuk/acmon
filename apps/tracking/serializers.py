from rest_framework import serializers

from . import models


class TripSerializer(serializers.ModelSerializer):

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


class RecordSerializer(serializers.ModelSerializer):

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
