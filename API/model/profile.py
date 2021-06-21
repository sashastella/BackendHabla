from django.contrib.auth.models import User
from django.db import models

from django.db.models import ManyToManyField


class Profile(models.Model):
    """
    Profile Details
    """

    phone = models.CharField(max_length=70)
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE, primary_key=True)
    roles = models.ManyToManyField("Role", related_name="profile_roles")

