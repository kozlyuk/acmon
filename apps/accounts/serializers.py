from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [
            "phone",
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
