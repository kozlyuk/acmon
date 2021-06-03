from rest_framework import serializers

from . import models


class TripSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Trip
        fields = [
            "last_updated",
            "created",
        ]


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Record
        fields = [
            "created",
            "last_updated",
        ]
