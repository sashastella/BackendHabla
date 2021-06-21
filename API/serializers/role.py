from rest_framework import serializers

from API.model.role import Role


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', 'description', 'status', 'created_at')

    def create(self, validate_data):
        instance = Role()
        instance.name = self.initial_data.get('name')
        instance.description = self.initial_data.get('description')
        instance.status = self.initial_data.get('status')
        instance.save()
        return instance

    def update(self):
        instance = Role.objects.get(id=self.initial_data.get('id'))
        instance.name = self.initial_data.get('name')
        instance.description = self.initial_data.get('description')
        instance.status = self.initial_data.get('status')
        instance.save()
        return instance


