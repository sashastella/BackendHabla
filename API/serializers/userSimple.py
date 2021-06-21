from django.contrib.auth.models import User
from rest_framework import serializers

from Common.enums import RequestType


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    requestType = None

    def set_requestType(self, type):
        self.requestType = type

    def update(self):
        instance = User.objects.get(id=self.initial_data.get('id'))
        instance.first_name = self.initial_data.get('first_name').capitalize()
        instance.last_name = self.initial_data.get('last_name').capitalize()
        if self.initial_data.get('password'):
            instance.set_password = self.initial_data.get('password')
        instance.save()
        return instance

    def validate_email(self, data):
        users = User.objects.filter(email=data)
        if len(users) != 0 and self.requestType == RequestType.POST:
            raise serializers.ValidationError("Este correo ya existe")
        else:
            return data

