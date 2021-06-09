from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "mobile_number",
            "lang",
            "birth_date",
            "avatar",
            "is_registered",
            "is_staff",
            "is_active",
        ]


# class OperatorSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = models.Operator
#         fields = [
#         ]

# class DriverSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = models.Driver
#         fields = [
#         ]
