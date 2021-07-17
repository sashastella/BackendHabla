from rest_framework import serializers

from API.model.anamnesis import Anamnesis


class AnamnesisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anamnesis
        fields = ('id', 'motive', 'genogram', 'history', 'emotional', 'physical', 'labor_details', 'motor_des',
                  'language_des', 'cognitive_des', 'adaptation', 'personality', 'interpersonal', 'distractions',
                  'events', 'sexuality', 'scholar_act', 'parents_imp', 'familiar_ant', 'familiar_din', 'socioeconomic',
                  'general_imp', 'created_at')

    def create(self, validate_data):
        instance = Anamnesis()
        instance.motive = self.initial_data.get('motive')
        instance.genogram = self.initial_data.get('genogram')
        instance.history = self.initial_data.get('history')
        instance.emotional = self.initial_data.get('emotional')
        instance.physical = self.initial_data.get('physical')
        instance.labor_details = self.initial_data.get('labor_details')
        instance.motor_des = self.initial_data.get('motor_des')
        instance.language_des = self.initial_data.get('language_des')
        instance.cognitive_des = self.initial_data.get('cognitive_des')
        instance.adaptation = self.initial_data.get('adaptation')
        instance.personality = self.initial_data.get('personality')
        instance.interpersonal = self.initial_data.get('interpersonal')
        instance.distractions = self.initial_data.get('distractions')
        instance.events = self.initial_data.get('events')
        instance.sexuality = self.initial_data.get('sexuality')
        instance.scholar_act = self.initial_data.get('scholar_act')
        instance.parents_imp = self.initial_data.get('parents_imp')
        instance.familiar_ant = self.initial_data.get('familiar_ant')
        instance.familiar_din = self.initial_data.get('familiar_din')
        instance.socioeconomic = self.initial_data.get('socioeconomic')
        instance.general_imp = self.initial_data.get('general_imp')
        instance.save()
        return instance

    def update(self):
        instance = Anamnesis.objects.get(id=self.initial_data.get('id'))
        instance.motive = self.initial_data.get('motive')
        instance.genogram = self.initial_data.get('genogram')
        instance.history = self.initial_data.get('history')
        instance.emotional = self.initial_data.get('emotional')
        instance.physical = self.initial_data.get('physical')
        instance.labor_details = self.initial_data.get('labor_details')
        instance.motor_des = self.initial_data.get('motor_des')
        instance.language_des = self.initial_data.get('language_des')
        instance.cognitive_des = self.initial_data.get('cognitive_des')
        instance.adaptation = self.initial_data.get('adaptation')
        instance.personality = self.initial_data.get('personality')
        instance.interpersonal = self.initial_data.get('interpersonal')
        instance.distractions = self.initial_data.get('distractions')
        instance.events = self.initial_data.get('events')
        instance.sexuality = self.initial_data.get('sexuality')
        instance.scholar_act = self.initial_data.get('scholar_act')
        instance.parents_imp = self.initial_data.get('parents_imp')
        instance.familiar_ant = self.initial_data.get('familiar_ant')
        instance.familiar_din = self.initial_data.get('familiar_din')
        instance.socioeconomic = self.initial_data.get('socioeconomic')
        instance.general_imp = self.initial_data.get('general_imp')
        instance.save()
        return instance
