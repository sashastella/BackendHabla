from datetime import datetime

from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from API.model.profile import Profile
from API.serializers.profile import ProfileSerializer
from API.serializers.role import RoleSerializer
from API.serializers.user import UserSerializer
from API.serializers.userSimple import UserSimpleSerializer

UserSerializer
UserSimpleSerializer
ProfileSerializer
RoleSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])
        if user is not None:
            if user.is_active:
                data = super().validate(attrs)
                refresh = self.get_token(self.user)
                refresh['username'] = self.user.username
                try:
                    obj = Profile.objects.get(user=self.user)
                    refresh['type'] = obj.type
                    data["refresh"] = str(refresh)
                    data["access"] = str(refresh.access_token)
                    data["employee_id"] = self.user.id
                    data['user_name'] = self.user.username
                    data["type"] = obj.type
                    data['first_name'] = self.user.first_name
                    data['last_name'] = self.user.last_name
                    user.last_login = datetime.datetime.now()
                    user.save()
                except Exception as e:
                    raise serializers.ValidationError('Something Wrong!')
                return data
            else:
                raise serializers.ValidationError('Account is Blocked')
        else:
            raise serializers.ValidationError('Incorrect userid/email and password combination!')


class TokenCheck(serializers.Serializer):
    token = serializers.CharField()