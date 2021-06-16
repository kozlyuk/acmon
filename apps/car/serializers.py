from rest_framework import serializers

from . import models
from apps.tracking.models import Record
from apps.tracking.serializers import RecordSerializer


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Brand
        fields = [
            "id",
            "name",
            "last_updated",
            "updated_at",
            "created_at",
        ]

class CarSerializer(serializers.ModelSerializer):

    last_position = serializers.SerializerMethodField()

    class Meta:
        model = models.Car
        fields = [
            "id",
            "model",
            "department",
            "sim_imei",
            "sim_number",
            "number",
            "color",
            "is_active",
            "updated_at",
            "created_at",
            "last_position",
        ]

    def get_last_position(self, obj):
        try:
            return RecordSerializer(obj.record_set.latest()).data
        except Record.DoesNotExist:
            return None


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Company
        fields = [
            "id",
            "name",
            "contact_person",
            "contact_phone",
            "email",
            "updated_at",
            "created_at",
        ]

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Department
        fields = [
            "id",
            "company",
            "name",
            "updated_at",
            "created_at",
        ]

class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Model
        fields = [
            "id",
            "brand",
            "name",
            "year_of_production",
            "updated_at",
            "created_at",
        ]
