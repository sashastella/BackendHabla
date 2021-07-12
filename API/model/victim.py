from django.db import models

from django.db.models import ManyToManyField


class Victim(models.Model):
    """
    Victim Details
    """

    expedient_number = models.CharField(max_length=70)
    name = models.CharField(max_length=70)
    second_name = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    birthdate = models.DateField()
    age = models.IntegerField()
    address = models.CharField(max_length=500)
    occupation = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=70)
    phone_number2 = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    reference = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
