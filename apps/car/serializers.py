from rest_framework import serializers

from . import models


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Brand
        fields = [
            "name",
            "last_updated",
            "created",
        ]

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Car
        fields = [
            "last_updated",
            "created",
        ]

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Company
        fields = [
            "last_updated",
            "contact_person",
            "billing_email",
            "created",
            "contact_phone",
            "name",
        ]

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Department
        fields = [
            "created",
            "name",
            "last_updated",
        ]

class ModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Model
        fields = [
            "name",
            "last_updated",
            "created",
        ]
