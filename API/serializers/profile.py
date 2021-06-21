from django.contrib.auth.models import User
from rest_framework import serializers

from API.model.profile import Profile
from API.model.role import Role
from API.serializers.role import RoleSerializer
from API.serializers.user import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user_id', 'phone', 'status', 'created_at', 'roles', 'profile')

    profile = serializers.SerializerMethodField('_get_children')
    roles = serializers.SerializerMethodField('_get_roles')
    requestType = None
    user = None

    def _get_children(self, obj):
        if self.user is not None:
            user = User.objects.get(id=self.user.id)
        else:
            user = User.objects.get(id=obj.user_id) #en caaso de ser many se cambia el get por filter
        serializer = UserSerializer(user) #en caso de ser many poner el parametro a UserSerializer(user, many=True)
        return serializer.data

    def _get_roles(self, obj):
        roles = Role.objects.filter(profile_roles__user_id=obj.user_id)
        if roles:
            serializer = RoleSerializer(roles, many=True)
            return serializer.data
        else:
            return ""

    def set_requestType(self, type):
        self.requestType = type

    def set_user(self, user):
        self.user = user

    def create(self, validate_data):
        instance = Profile()
        instance.status = self.initial_data.get('status')
        instance.phone = self.initial_data.get('phone')
        instance.user = self.user
        instance.save()

        roles = self.initial_data.get('roles')
        for role in roles:
            data = Role.objects.get(pk=role.get('id'))
            instance.roles.add(data)
        return instance

    def update(self):
        instance = Profile.objects.get(user=self.user)
        instance.status = self.initial_data.get("status")
        instance.phone = self.initial_data.get('phone')
        instance.save()

        roles = self.initial_data.get('roles')
        for role in roles:
            instance.roles.clear()
            data = Role.objects.get(pk=role.get('id'))
            instance.roles.add(data)
        return instance