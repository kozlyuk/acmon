from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from . import models


class UserSerializer(serializers.ModelSerializer):
    """A Serizlier class for User """
    password = serializers.CharField(required=True)

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
            "password",
            "is_registered",
            "is_staff",
            "is_active",
        ]
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password' : {'write_only' : True},
            }

    def create(self, validated_data):
        # creating user and adding it to groups
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        validated_data['is_active'] = False
        user = models.User.objects.create(**validated_data)
        return user

    def update(self, instance, validated_data):
        # updating user
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.mobile_number = validated_data.get('email', instance.mobile_number)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.lang = validated_data.get('lang', instance.lang)
        if 'password' in validated_data:
            instance.password = make_password(validated_data['password'])
        instance.save()

        return instance
