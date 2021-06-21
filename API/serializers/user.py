from django.contrib.auth.models import User
from rest_framework import serializers

from Common.enums import RequestType


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')

    requestType = None

    def set_requestType(self, type):
        self.requestType = type

    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get('first_name').capitalize()
        instance.last_name = validate_data.get('last_name').capitalize()
        instance.username = validate_data.get('email')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance

    def validate_password(self, data):
        if data:
            return data
        else:
            return data

    def validate_email(self, data):
        users = User.objects.filter(email=data)
        if len(users) != 0 and self.requestType == RequestType.POST:
            raise serializers.ValidationError("Este correo ya existe")
        else:
            return data
