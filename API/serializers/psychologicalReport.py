from rest_framework import serializers

from API.model.psychologicalReport import PsychologicalReport


class PsychologicalReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PsychologicalReport
        fields = ('id', 'motive','instruments', 'genogram', 'personal_ant', 'familiar_ant', 'general_imp',
                  'mental_exam', 'results', 'created_at')

    def create(self, validate_data):
        instance = PsychologicalReport()
        instance.motive = self.initial_data.get('motive')
        instance.instruments = self.initial_data.get('instruments')
        instance.genogram = self.initial_data.get('genogram')
        instance.personal_ant = self.initial_data.get('personal_ant')
        instance.familiar_ant = self.initial_data.get('familiar_ant')
        instance.general_imp = self.initial_data.get('general_imp')
        instance.mental_exam = self.initial_data.get('mental_exam')
        instance.results = self.initial_data.get('results')
        instance.save()
        return instance

    def update(self):
        instance = PsychologicalReport.objects.get(id=self.initial_data.get('id'))
        instance.motive = self.initial_data.get('motive')
        instance.instruments = self.initial_data.get('instruments')
        instance.genogram = self.initial_data.get('genogram')
        instance.personal_ant = self.initial_data.get('personal_ant')
        instance.familiar_ant = self.initial_data.get('familiar_ant')
        instance.general_imp = self.initial_data.get('general_imp')
        instance.mental_exam = self.initial_data.get('mental_exam')
        instance.results = self.initial_data.get('results')
        instance.save()
        return instance
