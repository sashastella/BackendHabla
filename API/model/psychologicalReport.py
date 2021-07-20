from django.db import models

from django.db.models import ManyToManyField


class PsychologicalReport(models.Model):
    """
    PsychologicalReport Details
    """

    motive = models.CharField(max_length=200)
    instruments = models.CharField(max_length=5000)
    genogram = models.CharField(max_length=500)
    personal_ant = models.CharField(max_length=500)
    familiar_ant = models.CharField(max_length=500)
    general_imp = models.CharField(max_length=500)
    mental_exam = models.CharField(max_length=500)
    results = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)