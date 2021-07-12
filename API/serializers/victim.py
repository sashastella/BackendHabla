from rest_framework import serializers

from API.model.victim import Victim


class VictimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Victim
        fields = ('id', 'expedient_number', 'name', 'second_name', 'lastname', 'birthdate', 'age', 'address',
                  'occupation', 'phone_number', 'phone_number2', 'email', 'reference', 'created_at')

    def create(self, validate_data):
        instance = Victim()
        instance.expedient_number = self.initial_data.get('expedient_number')
        instance.name = self.initial_data.get('name')
        instance.second_name = self.initial_data.get('second_name')
        instance.lastname = self.initial_data.get('lastname')
        instance.birthdate = self.initial_data.get('birthdate')
        instance.age = self.initial_data.get('age')
        instance.address = self.initial_data.get('address')
        instance.occupation = self.initial_data.get('occupation')
        instance.phone_number = self.initial_data.get('phone_number')
        instance.phone_number2 = self.initial_data.get('phone_number2')
        instance.email = self.initial_data.get('email')
        instance.reference = self.initial_data.get('reference')
        instance.save()
        return instance

    def update(self):
        instance = Victim.objects.get(id=self.initial_data.get('id'))
        instance.expedient_number = self.initial_data.get('expedient_number')
        instance.name = self.initial_data.get('name')
        instance.second_name = self.initial_data.get('second_name')
        instance.lastname = self.initial_data.get('lastname')
        instance.birthdate = self.initial_data.get('birthdate')
        instance.age = self.initial_data.get('age')
        instance.address = self.initial_data.get('address')
        instance.occupation = self.initial_data.get('occupation')
        instance.phone_number = self.initial_data.get('phone_number')
        instance.phone_number2 = self.initial_data.get('phone_number2')
        instance.email = self.initial_data.get('email')
        instance.reference = self.initial_data.get('reference')
        instance.save()
        return instance