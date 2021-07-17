from django.db import models

from django.db.models import ManyToManyField


class Anamnesis(models.Model):
    """
    Anamnesis Details
    """

    motive = models.CharField(max_length=200)
    genogram = models.CharField(max_length=500)
    history = models.CharField(max_length=5000)
    emotional = models.CharField(max_length=500)
    physical = models.CharField(max_length=500)
    labor_details = models.CharField(max_length=500)
    motor_des = models.CharField(max_length=500)
    language_des = models.CharField(max_length=500)
    cognitive_des = models.CharField(max_length=500)
    adaptation = models.CharField(max_length=500)
    personality = models.CharField(max_length=500)
    interpersonal = models.CharField(max_length=500)
    distractions = models.CharField(max_length=500)
    events = models.CharField(max_length=500)
    sexuality = models.CharField(max_length=500)
    scholar_act = models.CharField(max_length=500)
    parents_imp = models.CharField(max_length=500)
    familiar_ant = models.CharField(max_length=500)
    familiar_din = models.CharField(max_length=500)
    socioeconomic = models.CharField(max_length=500)
    general_imp = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)